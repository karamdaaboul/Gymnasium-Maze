import gymnasium as gym
import gymnasium_robotics
import pygame
import time
import numpy as np

from gymnasium_maze.ui import TeleopGamepadPoint2D 
from gymnasium_maze.envs.wrappers.intervention_wrappers import HumanInterventionWrapper           

def main():
    # --- 2. Setup the Base Environment ---
    env = gym.make(
        'PointMaze_Medium_Dangerous-v3', 
        continuing_task=False,
        render_mode="human",
        max_episode_steps=500
    )

    try:
        # --- 3. Setup the Teleoperation Interface ---
        # Initialize the class imported from the library
        teleop_agent = TeleopGamepadPoint2D(deadzone=0.1)

        # --- 4. Wrap the Environment ---
        # The wrapper takes the base environment and the teleop interface.
        env = HumanInterventionWrapper(
            env,
            teleop_agent,
            threshold=0.2,  # Start override if joystick moves > 10%
            hold_time=0.1   # Stay in override mode for 0.5s after last input
        )

        # --- 5. Main Loop ---
        obs, info = env.reset()
        
        running = True
        while running:
            # This simulates a simple, autonomous policy (e.g., your RL agent's output)
            # Here, it's just a random action.
            random_policy_action = env.action_space.sample()
            # The step function now takes the policy's action as an argument.
            # The wrapper will decide whether to use it or the human's action.
            obs, reward, terminated, truncated, info = env.step(random_policy_action)

            # Check if the Pygame window was closed
            # Note: This is necessary because the Teleop class initializes pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Print override status for demonstration
            if info.get("human_override", False):
                # Using .round(2) for cleaner printing
                human_action_str = np.array2string(info['intervene_action'], formatter={'float_kind':lambda x: "%.2f" % x})
                print(f"\rHuman override ACTIVE! Action: {human_action_str}", end="")
            else:
                policy_action_str = np.array2string(random_policy_action, formatter={'float_kind':lambda x: "%.2f" % x})
                print(f"\rPolicy ACTIVE!        Action: {policy_action_str}", end="")

            if terminated or truncated:
                print("\nEpisode finished. Resetting...") # Newline to not overwrite the status line
                time.sleep(1)
                obs, info = env.reset()

            time.sleep(0.01)

    except (IOError, pygame.error) as e:
        print(f"\nError: {e}")
        print("Please ensure a joystick is connected and the 'gymnasium_maze' library is installed correctly.")
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        print("\nClosing environment.")
        env.close() # This will also close the base_env
        pygame.quit()

if __name__ == "__main__":
    # You might not need this line if gymnasium_robotics is already registered
    # by importing gymnasium_maze, but it's safe to keep.
    gym.register_envs(gymnasium_robotics) 
    main()