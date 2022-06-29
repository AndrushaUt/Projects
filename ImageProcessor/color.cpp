#include "color.h"
#include <algorithm>

Color Color::operator*(double num) const {
    Color other;
    other.blue = blue * double(num);
    other.green = green * double(num);
    other.red = red * double(num);
    return other;
}

Color &Color::operator+=(const Color &other) {
    red += other.red;
    green += other.green;
    blue += other.blue;
    return *this;
}

Color &Color::operator*=(const Color &other) {
    red *= other.red;
    green *= other.green;
    blue *= other.blue;
    return *this;
}

bool Color::operator>(double num) const {
    return red > num or blue > num or green > num;
}

void Color::SetColor(double num) {
    red = num;
    green = num;
    blue = num;
}

void Color::SetColorMin(double num) {
    red = std::min(red, num);
    green = std::min(green, num);
    blue = std::min(blue, num);
}

void Color::SetColorMax(double num, const Color& other) {
    red = std::max(other.red, num);
    green = std::max(other.green, num);
    blue = std::max(other.blue, num);
}

bool Color::operator==(double num) const {
    return (red <= num and red >= num) or (blue <= num and red >= blue) or (green <= num and green >= num);
}

Color &Color::operator*=(double num) {
    red *= num;
    green *= num;
    blue *= num;
    return *this;
}
