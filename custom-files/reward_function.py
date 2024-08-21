def reward_function(params):
    # Parameters available for use
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle'])
    ABS_STEERING_THRESHOLD = 13

    # Calculate the distance from the center as a fraction of the track width
    distance_from_center_ratio = distance_from_center / (track_width / 2)

    # Define the reward, encouraging the car to stay closer to the center
    if distance_from_center_ratio <= 0.1:
        reward = 1.0  # Optimal position close to the center
    elif distance_from_center_ratio <= 0.25:
        reward = 0.8  # Slightly off-center
    elif distance_from_center_ratio <= 0.5:
        reward = 0.5  # Moderately off-center
    else:
        reward = 0.001  # Close to the edge or off-track
 
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)