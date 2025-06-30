import pygame
import numpy as np
from collections import defaultdict

# -----------------------------------------------------------------------------
# PygameGamepad: A simple wrapper for reading joystick state.
# -----------------------------------------------------------------------------
class PygameGamepad:
    """
    Initializes a PyGame joystick and provides methods to read its state.
    This version is simplified to directly support the PointMaze environment.
    """
    def __init__(self):
        pygame.init()
        try:
            self.joy = pygame.joystick.Joystick(0)
            self.joy.init()
            print(f"[INFO] Detected Joystick: {self.joy.get_name()}")
            print(f"[INFO] Axes: {self.joy.get_numaxes()}, Buttons: {self.joy.get_numbuttons()}")
        except pygame.error:
            raise IOError("No joystick detected. Please connect a controller.")

    def get_axes(self):
        """
        Reads the raw axis values from the joystick.
        Returns a dictionary of relevant axis values in the range [-1.0, 1.0].
        """
        # This is crucial for updating the joystick state
        pygame.event.pump()

        # Standard mapping for most controllers (e.g., Xbox, PS4/5)
        # Left Stick X: -1 (left) to 1 (right)
        # Left Stick Y: -1 (up) to 1 (down) <-- Note: Pygame's Y is often inverted
        ax_x = self.joy.get_axis(0)
        ax_y = self.joy.get_axis(1)
        
        return {"x": ax_x, "y": ax_y}

    def get_buttons(self):
        """
        Reads the state of the face buttons and shoulder buttons.
        Returns a dictionary with boolean values.
        """
        pygame.event.pump()
        # Common button mapping for PlayStation controllers
        return {
            "cross":    bool(self.joy.get_button(0)),  # X button
            "circle":   bool(self.joy.get_button(1)),  # O button
            "square":   bool(self.joy.get_button(2)),
            "triangle": bool(self.joy.get_button(3)),
            "l1":       bool(self.joy.get_button(4)),
            "r1":       bool(self.joy.get_button(5)),
        }

# -----------------------------------------------------------------------------
# TeleopGamepadPoint2D: Main class for 2D teleoperation.
# -----------------------------------------------------------------------------
class TeleopGamepadPoint2D:
    """
    Reads joystick axes and converts them to a 2D action vector [force_x, force_y]
    for the PointMaze environment.
    
    The action space of PointMaze is Box(-1.0, 1.0, (2,)).
    - action[0]: Force in the x-direction.
    - action[1]: Force in the y-direction.
    """
    def __init__(self, deadzone=0.15):
        """
        Initializes the teleoperation agent.
        
        Args:
            deadzone (float): Stick inputs with an absolute value smaller than this
                              will be ignored (range 0.0 to 1.0).
        """
        self.deadzone = deadzone
        self.action = np.zeros(2, dtype=np.float32)
        self.device = PygameGamepad()

    def get_action(self):
        """
        Calculates and returns the 2D action vector based on joystick input.
        
        Returns:
            np.ndarray: A 2D numpy array [force_x, force_y] with values in [-1, 1].
        """
        axes = self.device.get_axes()
        
        # Raw stick values
        raw_x = axes.get("x", 0.0)
        raw_y = axes.get("y", 0.0)

        # Apply deadzone
        force_x = raw_x if abs(raw_x) > self.deadzone else 0.0
        
        # Invert the Y-axis for intuitive control (up on stick = positive y force)
        force_y = -raw_y if abs(raw_y) > self.deadzone else 0.0
        
        self.action[0] = force_x
        self.action[1] = force_y
        
        return self.action.copy()

    def get_button_states(self):
        """
        A helper function to pass through button states from the device.
        Useful for triggering events like resetting the environment.
        """
        return self.device.get_buttons()