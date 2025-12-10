import gymnasium as gym
import numpy as np
import random
import time

print("Kütüphaneler yüklendi . Akıllı Ajan (Q-Learning) başlıyor...")


env = gym.make("FrozenLake-v1", is_slippery=False)
print("Eğitim için 'FrozenLake' ortamı GÖRSEL OLMADAN yüklendi (hızlı mod).")

state_size = env.observation_space.n
action_size = env.action_space.n



q_table = np.zeros((state_size, action_size))

print(f"Q-Tablosu (Beyin) oluşturuldu. Boyut : {q_table.shape}")


total_episodes = 15000
learning_rate = 0.001
gamma = 0.9

epsilon = 1.0
max_epsilon = 5.0
min_epsilon = 0.03
decay_rate = 0.0009

print(f"Eğitim {total_episodes} bölüm (episode) boyunca başlıyor...")

start_time = time.time()

for episode in range(total_episodes):

    state, info = env.reset()
    terminated = False
    truncated = False

    while not terminated and not truncated:

        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state, :])


        new_state, reward, terminated, truncated, info = env.step(action)

        q_table[state, action] = q_table[state, action] + learning_rate * \
                                 (reward + gamma * np.max(q_table[new_state, :]) - q_table[state, action])
        state = new_state

    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

    if (episode + 1) % 1000 == 0:
        print(f"Bölüm {episode + 1}/{total_episodes} tamamlandı...")

end_time = time.time()
print(f"Eğitim tamamlandı. Süre : {end_time - start_time:.2f} saniye")

print("\n--- Öğrenilmiş Q-Tablosu (Ajanın Beyni) ---")
print(q_table)

print("\nEğitilmiş ajan test ediliyor...")

env_test = gym.make("FrozenLake-v1", render_mode="human", is_slippery=False)
total_wins = 0
total_test_episodes = 50

for episode in range(total_test_episodes):
    state, info = env_test.reset()
    terminated = False
    truncated = False
    print(f"--- Test Bölümü {episode + 1} ---")

    while not terminated and not truncated:
        action = np.argmax(q_table[state, :])

        new_state, reward, terminated, truncated, info = env_test.step(action)

        state = new_state

        time.sleep(0.15)

    if terminated and reward == 1.0:
        print("**** Ajan HEDEFE ulaştı! (Kazandı) ****")
        total_wins += 1

print(f"\nTest tamamlandı. {total_test_episodes} oyunda {total_wins} kez kazanıldı.")

env.close()
env_test.close()