# Python ile Q-Learning FrozenLake Akıllı Ajan

Bu projede Python ve Gymnasium kütüphanesi kullanılarak FrozenLake ortamında Q-Learning algoritması ile bir akıllı ajan eğitilmiş ve görsel ortamda test edilmiştir.

## 📋 İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Q-Learning Algoritması](#q-learning-algoritması)
- [Sonuçlar](#sonuçlar)
- [Lisans](#lisans)

## 🎯 Proje Hakkında

Bu proje, Reinforcement Learning (Pekiştirmeli Öğrenme) alanında popüler bir algoritma olan Q-Learning'i kullanarak FrozenLake ortamında bir ajan eğitmeyi amaçlamaktadır. Proje iki aşamadan oluşmaktadır:

1. **Adım 1**: Rastgele ajan ile FrozenLake ortamının test edilmesi
2. **Adım 2**: Q-Learning algoritması ile ajanın eğitilmesi ve test edilmesi

## 📦 Gereksinimler

- Python 3.7+
- gymnasium
- numpy
- pygame (görselleştirme için)

## 🚀 Kurulum

1. Projeyi klonlayın veya indirin:
```bash
git clone https://github.com/dogukanyarimel/frozenlake-qlearning-agent.git
cd frozenlake-qlearning-agent
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

## 💻 Kullanım

### Adım 1: Rastgele Ajan Testi

Rastgele hareketler yapan bir ajan ile FrozenLake ortamını test etmek için:

```bash
python adim_1_rastgele_ajan.py
```

Bu script, 50 bölüm boyunca rastgele hareketler yapan bir ajanı çalıştırır ve sonuçları görsel olarak gösterir.

### Adım 2: Q-Learning ile Eğitim ve Test

Q-Learning algoritması ile ajanı eğitmek ve test etmek için:

```bash
python adim_2_egitim_ve_test.py
```

Bu script:
- 15,000 bölüm boyunca ajanı eğitir (görsel olmadan, hızlı mod)
- Öğrenilmiş Q-tablosunu gösterir
- Eğitilmiş ajanı 50 test bölümünde görsel olarak test eder
- Başarı oranını raporlar

## 📁 Proje Yapısı

```
frozenlake-qlearning-agent/
│
├── adim_1_rastgele_ajan.py    # Rastgele ajan testi
├── adim_2_egitim_ve_test.py   # Q-Learning eğitimi ve testi
├── requirements.txt            # Python bağımlılıkları
├── README.md                   # Bu dosya
├── .gitignore                  # Git ignore dosyası
└── LICENSE                     # MIT Lisansı
```

## 🧠 Q-Learning Algoritması

Q-Learning, model-free bir reinforcement learning algoritmasıdır. Bu projede kullanılan parametreler:

- **Learning Rate (α)**: 0.001
- **Discount Factor (γ)**: 0.9
- **Epsilon (ε)**: 1.0 (başlangıç) → 0.03 (minimum)
- **Epsilon Decay**: 0.0009
- **Total Episodes**: 15,000

Q-Learning güncelleme formülü:
```
Q(s,a) = Q(s,a) + α * [r + γ * max(Q(s',a')) - Q(s,a)]
```

## 📊 Sonuçlar

Eğitim tamamlandıktan sonra, ajan FrozenLake ortamında hedefe ulaşmayı öğrenir. Test aşamasında, eğitilmiş ajan genellikle %90+ başarı oranı gösterir (is_slippery=False modunda).

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👤 Yazar

**Dogukan Yarimel**

- GitHub: [@dogukanyarimel](https://github.com/dogukanyarimel)

## 🙏 Teşekkürler

- [Gymnasium](https://gymnasium.farama.org/) - Reinforcement Learning ortamları için
- OpenAI - FrozenLake ortamı için ilham

