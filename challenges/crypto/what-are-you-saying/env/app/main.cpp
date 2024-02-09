#include <iostream>
#include <string>
#include <array>
#include <chrono>
#include <thread>


constexpr std::size_t POOL_SIZE = 100;

constexpr uint32_t fxor(uint32_t n) {
  n ^= n << 13;
  n ^= n >> 17;
  n ^= n << 5;
  return n;
}

template<uint32_t N, uint32_t Seed> 
struct generate_bit {
  static constexpr uint32_t prev_value = generate_bit<N - 1, Seed>::value;
  static constexpr uint32_t value = fxor(prev_value);
};

template<uint32_t Seed>
struct generate_bit<0, Seed> {
  static constexpr uint32_t value = fxor(Seed);
};

template<size_t... Is>
constexpr std::array<bool, sizeof...(Is)> create_bit_pool(std::index_sequence<Is...>) {
  return {{ static_cast<bool>(generate_bit<Is, 0xDEADC0DE>::value & 1)... }};
}

constexpr std::array<bool, POOL_SIZE> bits = create_bit_pool(std::make_index_sequence<POOL_SIZE>{});


constexpr int DOT_DURATION = 100000;
constexpr int DASH_DURATION = 6 * DOT_DURATION;

constexpr std::array<const char*, 26> morse = {
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--.."
};

template <char C>
struct char_to_morse {
  static constexpr const char* value = morse[C - 'a'];
};

template <char C>
constexpr void print_morse(std::size_t& idx) {
  const char* m = char_to_morse<C>::value;

  while (*m) {
    std::this_thread::sleep_for(std::chrono::microseconds(*m == '.' ? DOT_DURATION : DASH_DURATION));
    std::cout << bits[idx++ % POOL_SIZE];
    std::cout.flush();
    m++;
  }
  std::cout << ' ';
}

template <char... C>
constexpr void print_morse_sequence() {
  std::size_t idx = 0;
  (print_morse<C>(idx), ...);
};

int main() {
  print_morse_sequence<'i', 'm', 'n', 'o', 't', 'a', 'g', 'o', 'o', 'd', 'm', 'o', 'r', 's', 'e', 'c', 'o', 'd', 'e', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r'>();
  return 0;
}