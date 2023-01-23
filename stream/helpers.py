from django.shortcuts import get_object_or_404
from stream.models import Episode


def episode_has_next(pk=None):
    """
    Check if an episode has a next one
    :param pk:
    :return:
    """
    episode = get_object_or_404(Episode, pk=pk)
    next_episode = None
    episodes_in_same_season = Episode.objects.filter(season=episode.season)
    try:
        if episodes_in_same_season.exists():
            next_episode = episodes_in_same_season.get(episode_number=episode.episode_number + 1)
        return next_episode
    except Episode.DoesNotExist:
        return None


def episode_has_previous(pk=None):
    """
    Check if an episode has a previous one
    :param pk:
    :return:
    """
    episode = get_object_or_404(Episode, pk=pk)
    previous_episode = None
    episodes_in_same_season = Episode.objects.filter(season=episode.season)
    try:
        if episodes_in_same_season.exists():
            previous_episode = episodes_in_same_season.get(episode_number=episode.episode_number - 1)
        return previous_episode
    except Episode.DoesNotExist:
        return None
