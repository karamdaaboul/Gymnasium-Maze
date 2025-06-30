# noqa: D104
from gymnasium.envs.registration import register

from gymnasium_maze.core import GoalEnv
from gymnasium_maze.envs.locomaze import maps

__version__ = "1.4.0"


def register_robotics_envs():
    """Register only maze environment ID's to Gymnasium."""

    def _merge(a, b):
        a.update(b)
        return a

    for reward_type in ["sparse", "dense"]:
        suffix = "Dense" if reward_type == "dense" else ""
        kwargs = {
            "reward_type": reward_type,
        }

        # ----- AntMaze -----
        for version in ["v3", "v4", "v5"]:
            register(
                id=f"AntMaze_UMaze{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.U_MAZE}, kwargs),
                max_episode_steps=700,
            )
            register(
                id=f"AntMaze_Open{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.OPEN}, kwargs),
                max_episode_steps=700,
            )
            register(
                id=f"AntMaze_Open_Diverse_G{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.OPEN_DIVERSE_G}, kwargs),
                max_episode_steps=700,
            )
            register(
                id=f"AntMaze_Open_Diverse_GR{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.OPEN_DIVERSE_GR}, kwargs),
                max_episode_steps=700,
            )
            register(
                id=f"AntMaze_Medium{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.MEDIUM_MAZE}, kwargs),
                max_episode_steps=1000,
            )
            register(
                id=f"AntMaze_Medium_Diverse_G{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.MEDIUM_MAZE_DIVERSE_G}, kwargs),
                max_episode_steps=1000,
            )
            register(
                id=f"AntMaze_Medium_Diverse_GR{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.MEDIUM_MAZE_DIVERSE_GR}, kwargs),
                max_episode_steps=1000,
            )
            register(
                id=f"AntMaze_Large{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.LARGE_MAZE}, kwargs),
                max_episode_steps=1000,
            )
            register(
                id=f"AntMaze_Large_Diverse_G{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.LARGE_MAZE_DIVERSE_G}, kwargs),
                max_episode_steps=1000,
            )
            register(
                id=f"AntMaze_Large_Diverse_GR{suffix}-{version}",
                entry_point=f"gymnasium_maze.envs.locomaze.ant_maze_{version}:AntMazeEnv",
                kwargs=_merge({"maze_map": maps.LARGE_MAZE_DIVERSE_GR}, kwargs),
                max_episode_steps=1000,
            )

        # ----- PointMaze -----
        register(
            id=f"PointMaze_UMaze{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.U_MAZE}, kwargs),
            max_episode_steps=300,
        )
        register(
            id=f"PointMaze_Open{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.OPEN}, kwargs),
            max_episode_steps=300,
        )
        register(
            id=f"PointMaze_Open_Diverse_G{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.OPEN_DIVERSE_G}, kwargs),
            max_episode_steps=300,
        )
        register(
            id=f"PointMaze_Open_Diverse_GR{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.OPEN_DIVERSE_GR}, kwargs),
            max_episode_steps=300,
        )
        register(
            id=f"PointMaze_Medium{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.MEDIUM_MAZE}, kwargs),
            max_episode_steps=600,
        )
        register(
            id=f"PointMaze_Medium_Diverse_G{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.MEDIUM_MAZE_DIVERSE_G}, kwargs),
            max_episode_steps=600,
        )
        register(
            id=f"PointMaze_Medium_Diverse_GR{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.MEDIUM_MAZE_DIVERSE_GR}, kwargs),
            max_episode_steps=600,
        )
        register(
            id=f"PointMaze_Large{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.LARGE_MAZE}, kwargs),
            max_episode_steps=800,
        )
        register(
            id=f"PointMaze_Large_Diverse_G{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.LARGE_MAZE_DIVERSE_G}, kwargs),
            max_episode_steps=800,
        )
        register(
            id=f"PointMaze_Large_Diverse_GR{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.LARGE_MAZE_DIVERSE_GR}, kwargs),
            max_episode_steps=800,
        )
        register(
            id=f"PointMaze_Medium_Dangerous{suffix}-v3",
            entry_point="gymnasium_maze.envs.locomaze.point_maze:PointMazeEnv",
            kwargs=_merge({"maze_map": maps.MEDIUM_DANGEROUS_MAZE}, kwargs),
            max_episode_steps=600,
        )

register_robotics_envs()

try:
    import sys
    from farama_notifications import notifications
    if (
        "gymnasium_maze" in notifications
        and __version__ in notifications["gymnasium_maze"]
    ):
        print(notifications["gymnasium_maze"][__version__], file=sys.stderr)
except Exception:  # nosec
    pass
