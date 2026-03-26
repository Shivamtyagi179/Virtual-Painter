

    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]
        lmList = []
        for id, lm in enumerate(handLms.landmark):
            h, w, _ = img.shape