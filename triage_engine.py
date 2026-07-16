def run_triage(data: dict) -> dict:
    can_walk = data.get("can_walk", False)
    is_breathing = data.get("is_breathing", True)
    breathing_labored = data.get("breathing_labored", False)
    pulse_present = data.get("pulse_present", True)
    can_follow_commands = data.get("can_follow_commands", True)
    disaster_mode = data.get("disaster_mode", False)

    if not is_breathing:
        return {"severity": "RED", "reason": "Patient is not breathing. This is critical."}
    if breathing_labored:
        return {"severity": "RED", "reason": "Breathing is labored or abnormal rate."}
    if not pulse_present:
        return {"severity": "RED", "reason": "No pulse detected, poor circulation."}
    if not can_follow_commands:
        return {"severity": "RED", "reason": "Patient cannot follow simple commands."}
    if can_walk and not disaster_mode:
        return {"severity": "GREEN", "reason": "Patient is able to walk unaided."}
    if can_walk and disaster_mode:
        return {"severity": "YELLOW", "reason": "Patient can walk, but disaster conditions mean close monitoring is still needed."}
    return {"severity": "YELLOW", "reason": "Patient is stable but needs attention soon."}
