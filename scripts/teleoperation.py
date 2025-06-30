
import time
import pygame
import gymnasium as gym
import gymnasium_maze
from gymnasium_maze.ui import TeleopGamepadPoint2D


# Make sure to have the TeleopGamepadPoint2D class code in the same file
# or import it from teleop_point2d.py

def main():
    # 'd' marks a dangerous cell
    #DANGEROUS_LARGE_MAZE = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                        [1, 0, 0, 0, 0, 0, 0, 0, 1],
    #                        [1, 0, 1, 0, 1, 0, 1, "d", 1],
    #                        [1, 0, 0, "d", 1, 0, 0, 0, 1],
    #                        [1, 1, 1, 0, 1, 1, 1, 0, 1],
    #                        [1, 0, 1, 0, 0, 0, 0, 0, 1],
    #                        [1, 0, 1, 0, 1, "d", 1, 0, 1],
    #                        [1, 0, 0, 0, 1, 0, 0, 0, 1],
    #                        [1, 1, 1, 1, 1, 1, 1, 1, 1]]
#
#
    ## Initialize the environment
    #env = gym.make(
    #    'PointMaze_Large-v3', 
    #    maze_map=DANGEROUS_LARGE_MAZE,
    #    continuing_task=False,
    #    render_mode="human",
    #    max_episode_steps=500
    #)
    env = gym.make(
        'PointMaze_Medium_Dangerous-v3', 
        continuing_task=False,
        render_mode="human",
        max_episode_steps=500
    )

    try:
        # Initialize our 2D teleoperation agent
        agent = TeleopGamepadPoint2D(deadzone=0.2)
        print("Teleop agent initialized. Control the point with the left stick.")
        print("Press the 'X' button on the controller to reset the episode.")
        
        obs, info = env.reset()
        
        running = True
        while running:
            # --- Get Action from Joystick ---
            action = agent.get_action()

            # --- (Optional) Use buttons to control the simulation ---
            buttons = agent.get_button_states()
            if buttons.get("cross", False): # 'X' button on PS controller
                print("Reset button pressed. Resetting episode.")
                obs, info = env.reset()
                time.sleep(0.2) # Prevent multiple resets from one press

            # --- Step the Environment ---
            obs, reward, terminated, truncated, info = env.step(action)
            
            # --- Check for Episode End ---
            if terminated or truncated:
                if info.get("is_dangerous", False):
                    print("Episode terminated: Agent entered a dangerous zone!")
                else:
                    print("Episode finished. Resetting...")
                
                time.sleep(1) # Pause to show the result
                obs, info = env.reset()

            # The environment's render() is handled automatically by render_mode="human"
            # We add a small delay to not overload the CPU.
            time.sleep(0.02)

    except IOError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        print("Closing environment.")
        env.close()
        pygame.quit()

if __name__ == "__main__":
    gym.register_envs(gymnasium_maze)
    main()