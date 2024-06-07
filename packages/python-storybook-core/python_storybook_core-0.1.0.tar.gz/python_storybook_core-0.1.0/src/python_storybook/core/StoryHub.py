from typing import List, Dict, Union
from .utils import get_docs, get_type_hints
from python_storybook.core import (
    StoryManager, 
    Story, 
    StoryHub,
    StoryMeta
)


class StoryHub:
    _all_managers: Dict[str, StoryManager] = {}

    @staticmethod
    def register(story_manager: StoryManager) -> None:
        StoryHub._all_managers[story_manager.title] = story_manager

    @staticmethod
    def get_manager(title: str) -> StoryManager:
        for manager_title, manager in StoryHub._all_managers.items():
            if title == manager_title:
                return manager
        raise f"There is no StoryManager with the title: {title}."

    @staticmethod
    def get_titles() -> List[str]:
        titles = list(StoryHub._all_managers.keys())
        return titles

    @staticmethod
    def get_all_story_full_paths() -> List[str]:
        paths = []
        for manager in StoryHub._all_managers.values():
            paths.extend(manager.get_story_full_paths())
        return paths

    @staticmethod
    def get_story(full_path: str) -> Story:
        split = full_path.split("/")
        title = "/".join(split[:-1])
        story_name = split[-1]
        story_manager = StoryHub.get_manager(title)
        story = story_manager.get_story(story_name=story_name)
        return story

    @staticmethod
    def get_story_meta(story_or_path: Union[Story, str]) -> StoryMeta:
        if isinstance(story_or_path, Story):
            story = story_or_path
        elif isinstance(story_or_path, str):
            story = StoryHub.get_story(full_path=story_or_path)
        else:
            raise "invalid input."

        story_meta = StoryMeta(
            title=story.parent,
            name=story.name,
            func_name=story.func.__name__,
            docs=get_docs(story.func),
            type_hints=get_type_hints(story.func),
        )
        return story_meta

    @staticmethod
    def reset():
        StoryHub._all_managers.clear()
