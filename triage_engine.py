def run_triage(data: dict) -> dict:
    can_walk = data.get("can_walk", False)
    is_breathing = data.get("is_breathing", True)
    breathing_labored = data.get("breathing_labored", False)
    pulse_present = data.get("pulse_present", True)
    can_follow_commands = data.get("can_follow_commands", True)
    disaster_mode = data.get("disaster_mode", False)

    # 1. Critical Vital Signs Checks (RED / Immediate)
    if not is_breathing:
        return {"severity": "RED", "reason": "Patient is not breathing. Immediate airway intervention required."}
    if breathing_labored:
        return {"severity": "RED", "reason": "Breathing is labored or abnormal. Immediate respiratory support needed."}
    if not pulse_present:
        return {"severity": "RED", "reason": "No pulse detected. Sign of severe shock or circulatory failure."}
    if not can_follow_commands:
        return {"severity": "RED", "reason": "Patient is unresponsive or unable to follow simple commands. Indicates altered mental status."}

    # 2. Mobility Assessment (START Protocol)
    if can_walk:
        if disaster_mode:
            # Standard START protocol for mass casualties: ambulatory patients are categorized as GREEN (Minor) to optimize resources
            return {"severity": "GREEN", "reason": "Patient is ambulatory (can walk). Under disaster START protocol, they are classified as GREEN (Minor) to prioritize non-ambulatory victims."}
        else:
            # In normal, non-disaster emergency scenarios, any injured patient is monitored as YELLOW (Delayed/Urgent) for safety
            return {"severity": "YELLOW", "reason": "Patient is ambulatory but has reported symptoms. Rated as YELLOW for professional medical evaluation."}

    # 3. Non-ambulatory but stable (YELLOW / Delayed)
    return {"severity": "YELLOW", "reason": "Patient is stable (breathing, pulse, and mental status are normal) but unable to walk. Requires monitoring."}
