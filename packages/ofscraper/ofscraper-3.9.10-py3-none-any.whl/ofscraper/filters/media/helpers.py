import logging
import random
import re

import arrow

import ofscraper.utils.args.read as read_args
import ofscraper.utils.constants as constants
import ofscraper.utils.settings as settings
from ofscraper.utils.logs.helpers import is_trace
import ofscraper.utils.separate as seperate
from ofscraper.db.operations_.media import (
    get_media_ids_downloaded,
    get_media_ids_downloaded_model,
)

log = logging.getLogger("shared")


def sort_by_date(media):
    return sorted(media, key=lambda x: x.date)


def dupefilter(media):
    output = []
    ids = set()
    for item in media:
        if not item.id or item.id not in ids:
            output.append(item)
            ids.add(item.id)
    return output


def post_datesorter(output):
    return list(sorted(output, key=lambda x: x.date, reverse=True))


def timeline_array_filter(posts):
    out = []
    undated = list(filter(lambda x: x.get("postedAt") is None, posts))
    dated = list(filter(lambda x: x.get("postedAt") is not None, posts))
    dated = sorted(dated, key=lambda x: arrow.get(x.get("postedAt")))
    if read_args.retriveArgs().before:
        dated = list(
            filter(
                lambda x: arrow.get(x.get("postedAt"))
                <= read_args.retriveArgs().before,
                dated,
            )
        )
    if read_args.retriveArgs().after:
        dated = list(
            filter(
                lambda x: arrow.get(x.get("postedAt")) >= read_args.retriveArgs().after,
                dated,
            )
        )
    out.extend(undated)
    out.extend(dated)
    return out


def ele_count_filter(media):
    count = settings.get_max_post_count() or None
    return media[:count]


def posts_type_filter(media):
    filtersettings = settings.get_mediatypes()
    if isinstance(filtersettings, str):
        filtersettings = filtersettings.split(",")
    if isinstance(filtersettings, list):
        filtersettings = list(map(lambda x: x.lower().replace(" ", ""), filtersettings))
        filtersettings = list(filter(lambda x: x != "", filtersettings))
        if len(filtersettings) == 0:
            return media
        log.info(f"filtering Media to {','.join(filtersettings)}")
        media = list(filter(lambda x: x.mediatype.lower() in filtersettings, media))
    else:
        log.info("The settings you picked for the filter are not valid\nNot Filtering")
        log.debug(f"[bold]Combined Media Count Filtered:[/bold] {len(media)}")
    return media


def posts_date_filter_media(media):
    if read_args.retriveArgs().before:
        media = list(
            filter(
                lambda x: x.postdate is None
                or arrow.get(x.postdate) <= read_args.retriveArgs().before,
                media,
            )
        )
    if read_args.retriveArgs().after:
        media = list(
            filter(
                lambda x: x.postdate is None
                or arrow.get(x.postdate) >= read_args.retriveArgs().after,
                media,
            )
        )
    return media


def posts_date_filter(media):
    if read_args.retriveArgs().before:
        media = list(
            filter(
                lambda x: x.date is None
                or arrow.get(x.date) <= read_args.retriveArgs().before,
                media,
            )
        )
    if read_args.retriveArgs().after:
        media = list(
            filter(
                lambda x: x.date is None
                or arrow.get(x.date) >= read_args.retriveArgs().after,
                media,
            )
        )
    return media


def temp_post_filter(media):
    if read_args.retriveArgs().timed_only is False:
        return list(filter(lambda x: not x.expires, media))
    elif read_args.retriveArgs().timed_only is True:
        return list(filter(lambda x: x.expires, media))
    return media


def post_text_filter(media):
    userfilter = read_args.retriveArgs().filter
    if not userfilter:
        return media
    elif not userfilter.islower():
        return list(
            filter(lambda x: re.search(userfilter, x.text or "") is not None, media)
        )
    else:
        return list(
            filter(
                lambda x: re.search(userfilter, x.text or "", re.IGNORECASE)
                is not None,
                media,
            )
        )


def post_neg_text_filter(media):
    userfilter = read_args.retriveArgs().neg_filter
    if not userfilter:
        return media
    elif not userfilter.islower():
        return list(
            filter(lambda x: re.search(userfilter, x.text or "") is None, media)
        )
    else:
        return list(
            filter(
                lambda x: re.search(userfilter, x.text or "", re.IGNORECASE) is None,
                media,
            )
        )


def download_type_filter(media):
    if read_args.retriveArgs().protected_only:
        return list(filter(lambda x: x.protected, media))
    elif read_args.retriveArgs().normal_only:
        return list(filter(lambda x: not x.protected, media))
    else:
        return media


def mass_msg_filter(media):
    if read_args.retriveArgs().mass_msg is None:
        return media
    elif read_args.retriveArgs().mass_msg is True:
        return list((filter(lambda x: x.mass is True, media)))
    elif read_args.retriveArgs().mass_msg is False:
        return list((filter(lambda x: x.mass is False, media)))


def url_filter(media):
    return list((filter(lambda x: x.url or x.mpd, media)))

def unviewable_media_filter(media):
    return list(filter(lambda x: x.canview, media))


def final_post_sort(media):
    item_sort = read_args.retriveArgs().item_sort
    log.debug(f"Using download sort {item_sort}")
    if not item_sort:
        return media
    elif item_sort == "date-asc":
        return media
    elif item_sort == "date-desc":
        return list(reversed(media))
    elif item_sort == "random":
        random.shuffle(media)
        return media
    elif item_sort == "text-asc":
        return sorted(media, key=lambda x: x.text)
    elif item_sort == "text-desc":
        return sorted(media, key=lambda x: x.text, reverse=True)
    elif item_sort == "filename-asc":
        return sorted(media, key=lambda x: x.filename)
    elif item_sort == "filename-desc":
        return sorted(media, key=lambda x: x.filename, reverse=True)
def previous_download_filter(medialist,username=None,model_id=None):
    log = logging.getLogger("shared")
    log.info("reading database to retrive previous downloads")
    medialist = seperate.seperate_by_self(medialist)
    if read_args.retriveArgs().force_all:
        log.info("forcing all media to be downloaded")
    elif read_args.retriveArgs().force_model_unique:
        log.info("Downloading unique media for model")
        media_ids = set(
            get_media_ids_downloaded_model(model_id=model_id, username=username)
        )
        log.debug(
            f"Number of unique media ids in database for {username}: {len(media_ids)}"
        )
        medialist = seperate.separate_by_id(medialist, media_ids)
        log.debug(f"Number of new mediaids with dupe ids removed: {len(medialist)}")
        medialist = seperate.seperate_avatars(medialist)
        log.debug("Removed previously downloaded avatars/headers")
        log.debug(f"Final Number of media to download {len(medialist)}")
    else:
        log.info("Downloading unique media across all models")
        media_ids = set(get_media_ids_downloaded(model_id=model_id, username=username))
        log.debug("Number of unique media ids in database for all models")
        medialist = seperate.separate_by_id(medialist, media_ids)
        log.debug(f"Number of new mediaids with dupe ids removed: {len(medialist)}")
        medialist = seperate.seperate_avatars(medialist)
        log.debug("Removed previously downloaded avatars/headers")
        log.debug(f"Final Number of media to download {len(medialist)} ")
    logging.getLogger().info(f"Final media count for download {len(medialist)}")
    return medialist



def trace_log_media(count, media, filter_str):
    if not is_trace():
        return
    chunk_size = constants.getattr("LARGE_TRACE_CHUNK_SIZE")
    logformater = "{} id: {} postid: {} data: {} "
    for i in range(1, len(media) + 1, chunk_size):
        # Calculate end index considering potential last chunk being smaller
        end_index = min(i + chunk_size - 1, len(media))  # Adjust end_index calculation
        chunk = media[i - 1 : end_index]  # Adjust slice to start at i-1
        log.trace(
            "\n\n\n".join(
                map(
                    lambda x: logformater.format(
                        f"filter {count}-> {filter_str} ",
                        x.id,
                        x.postid,
                        x.media,
                    ),
                    chunk,
                )
            )
        )
        # Check if there are more elements remaining after this chunk
        if i + chunk_size > len(media):
            break  # Exit the loop if we've processed all elements


def trace_log_post(count, media, filter_str):
    if not is_trace():
        return
    chunk_size = constants.getattr("LARGE_TRACE_CHUNK_SIZE")
    logformater = "{} id: {} data: {} "
    for i in range(1, len(media) + 1, chunk_size):
        # Calculate end index considering potential last chunk being smaller
        end_index = min(i + chunk_size - 1, len(media))  # Adjust end_index calculation
        chunk = media[i - 1 : end_index]  # Adjust slice to start at i-1
        log.trace(
            "\n\n\n".join(
                map(
                    lambda x: logformater.format(
                        f"filter {count}-> {filter_str} ", x.id, x.post
                    ),
                    chunk,
                )
            )
        )
        # Check if there are more elements remaining after this chunk
        if i + chunk_size > len(media):
            break  # Exit the loop if we've processed all elements
