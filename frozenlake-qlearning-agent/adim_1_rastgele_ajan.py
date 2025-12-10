import gymnasium as gym
import time
import numpy as np

print("Kütüphaneler yüklendi.")





try:
    env = gym.make(("FrozenLake-v1") , render_mode="human",is_slippery=False)
    print("Gymnasium 'FrozenLake' ortamı başarıyla oluşturuldu.")
except Exception as e :
    print(f"Hata : Ortam oluşturulamadı.  'pygame' yüklü mü? Hata mesajı : {e}")
    exit()


print(f"Eylem :uzayı (Olası HAreket): {env.action_space.n}")
print(f"Durum Uzayı (Olası Hareket): {env.observation_space.n}")

num_episodes = 50

print(f"{num_episodes} bölüm (episode) oynanacak...")

for i in range(num_episodes):
    state , info = env.reset()
    print(f"--Bölüm {i+1} Başladı --- (Başlangıç Durumu : {state})")

    terminated = False
    truncated = False

    while not terminated and not truncated:

        action = env.action_space.sample()

        new_state , reward , terminated , truncated , info = env.step(action)

        state = new_state

        time.sleep(0.2)

    print(f"--- Bölüm {i+1} Bitti ---")
    if reward == 1:
        print("    Sonuç : Kazandı! (Hedefe ulaştı)")
    else:
        print("    Sonuç : Kaybetti. (Deliğe düştü)")

    time.sleep(1)


print("Tüm bölümler tamamlandı.Ortam kapatılıyor.")
env.close()

