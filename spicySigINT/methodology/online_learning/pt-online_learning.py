def online_learning(policy_network, env):
    state = env.reset()
    while True:
        action = policy_network.select_action(state)
        next_state, reward, done, _ = env.step(action)
        update_policy_online(policy_network, state, action, reward, next_state)
        if done:
            state = env.reset()
        else:
            state = next_state