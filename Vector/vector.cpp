#include "vector.h"
#include <algorithm>

Vector::Iterator::Iterator(Vector::ValueType* pointer) : iterator_{pointer} {
}

Vector::Iterator::Iterator() : iterator_{nullptr} {
}

Vector::ValueType& Vector::Iterator::operator*() const {
    return *iterator_;
}

Vector::ValueType* Vector::Iterator::operator->() const {
    return iterator_;
}

Vector::Iterator& Vector::Iterator::operator=(Vector::Iterator other) {
    iterator_ = other.iterator_;
    return *this;
}

Vector::Iterator& Vector::Iterator::operator++() {
    iterator_ += 1;
    return *this;
}

Vector::Iterator Vector::Iterator::operator++(int) {
    Vector::Iterator copy_of_iterator = *this;
    iterator_ += 1;
    return copy_of_iterator;
}

Vector::Iterator& Vector::Iterator::operator--() {
    iterator_ -= 1;
    return *this;
}

Vector::Iterator Vector::Iterator::operator--(int) {
    Vector::Iterator copy_of_iterator = *this;
    iterator_ -= 1;
    return copy_of_iterator;
}

Vector::Iterator Vector::Iterator::operator+(Vector::DifferenceType shift) {
    Vector::Iterator new_iterator;
    new_iterator.iterator_ = iterator_ + shift;
    return new_iterator;
}

Vector::DifferenceType Vector::Iterator::operator-(Vector::Iterator other) {
    return iterator_ - other.iterator_;
}

Vector::Iterator& Vector::Iterator::operator+=(Vector::DifferenceType shift) {
    iterator_ += shift;
    return *this;
}

Vector::Iterator& Vector::Iterator::operator-=(Vector::DifferenceType shift) {
    iterator_ -= shift;
    return *this;
}
bool Vector::Iterator::operator==(const Vector::Iterator& other) const {
    return iterator_ == other.iterator_;
}
bool Vector::Iterator::operator!=(const Vector::Iterator& other) const {
    return iterator_ != other.iterator_;
}
std::strong_ordering Vector::Iterator::operator<= >(const Vector::Iterator& other) const {
    return iterator_ <= > other.iterator_;
}

Vector::Vector(size_t size) : size_{size}, capacity_{size}, arr_{new ValueType[size]()} {
}

Vector::Vector() : size_{0}, capacity_{0}, arr_{nullptr} {
}

Vector::Vector(std::initializer_list<ValueType> list)
    : size_{list.size()}, capacity_{list.size()}, arr_{new ValueType[size_]} {
    size_t i = 0;
    for (const auto& init : list) {
        arr_[i] = init;
        ++i;
    }
}

Vector::Vector(const Vector& other)
    : size_{other.size_}, capacity_{other.capacity_}, arr_{new ValueType[other.capacity_]} {
    for (size_t i = 0; i < other.size_; i++) {
        arr_[i] = other.arr_[i];
    }
}

Vector::~Vector() {
    delete[] arr_;
}

Vector& Vector::operator=(const Vector& other) {
    if (this == &other) {
        return *this;
    }
    ValueType* temp_arr = new ValueType[other.capacity_];
    for (size_t i = 0; i < size_; i++) {
        temp_arr[i] = other.arr_[i];
    }
    delete[] arr_;
    arr_ = temp_arr;
    size_ = other.size_;
    capacity_ = other.capacity_;
    delete[] temp_arr;
    return *this;
}

Vector::SizeType Vector::Size() const {
    return size_;
}

Vector::SizeType Vector::Capacity() const {
    return capacity_;
}

const Vector::ValueType* Vector::Data() const {
    return arr_;
}

Vector::ValueType& Vector::operator[](size_t position) {
    return arr_[position];
}

Vector::ValueType Vector::operator[](size_t position) const {
    return arr_[position];
}

bool Vector::operator==(const Vector& other) const {
    if (size_ != other.size_) {
        return false;
    }
    for (size_t i = 0; i < size_; i++) {
        if (arr_[i] != other.arr_[i]) {
            return false;
        }
    }
    return true;
}

bool Vector::operator!=(const Vector& other) const {
    return !(*this == other);
}

void Vector::Reserve(Vector::SizeType new_capacity) {
    if (capacity_ < new_capacity) {
        ValueType* temp_arr = new int[new_capacity];
        for (size_t i = 0; i < size_; i++) {
            temp_arr[i] = arr_[i];
        }
        delete[] arr_;
        arr_ = temp_arr;
        capacity_ = new_capacity;
    }
}

void Vector::PushBack(const Vector::ValueType& new_element) {
    if (capacity_ <= size_) {
        if (capacity_ == 0) {
            Reserve(1);
        } else {
            Reserve(capacity_ * 2);
        }
    }
    arr_[size_] = new_element;
    size_ += 1;
}

void Vector::Clear() {
    size_ = 0;
}

void Vector::PopBack() {
    size_ -= 1;
}

void Vector::Swap(Vector& other) {
    std::swap(arr_, other.arr_);
    std::swap(size_, other.size_);
    std::swap(capacity_, other.capacity_);
}

std::strong_ordering Vector::operator<= >(const Vector& other) const {
    for (size_t i = 0; i < std::min(size_, other.size_); ++i) {
        if (arr_[i] != other.arr_[i]) {
            return arr_[i] <= > other.arr_[i];
        }
    }
    return size_ <= > other.size_;
}

Vector::Iterator Vector::begin() {
    return Vector::Iterator(arr_);
}

Vector::Iterator Vector::Begin() {
    return Vector::Iterator(arr_);
}

Vector::Iterator Vector::end() {
    return Vector::Iterator(arr_ + size_);
}

Vector::Iterator Vector::End() {
    return Vector::Iterator(arr_ + size_);
}
