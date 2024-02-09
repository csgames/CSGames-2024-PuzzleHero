#include <iostream>
#include <cmath>
#include <random>
#include <vector>
#include <iomanip>
#include <limits>


union float_bits {
    float value;
    uint32_t bits;

    explicit float_bits(float value) : value(value) {}
};

void print_float_bits(float val) {
  float_bits f(val);
  for (int i = 31; i >= 0; i--) {
    std::cout << ((f.bits >> i) & 1);
    if (i == 31 || i == 23) {
      std::cout << " ";
    }
  }
  std::cout << std::endl;
}

float generator(float val, unsigned char exponent) {
  float_bits f(val);

  uint32_t mask = 0x7F800000;
  f.bits &= ~mask;

  f.bits |= ((exponent & 0xFF) << 23);

  return f.value;
}



int main() {
  std::random_device rd; 
  std::mt19937 gen(rd()); 
  std::uniform_real_distribution<> dis(-42.0f, 42.0f);
  
  std::string flag = "flag{TrU5t_m3_1m_@n_3nG1n33r}";
  std::vector<float> floats;

  for (const auto& c : flag) {
    floats.push_back(generator(dis(gen), c));
  }

  for (const auto& f : floats) {
    std::cout << std::fixed << std::setprecision(std::numeric_limits<float>::max_exponent10) << f << std::endl;
  }
  return 0;
}