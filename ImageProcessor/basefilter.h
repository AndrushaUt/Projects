#pragma once

#include <unordered_map>
#include <string_view>
#include <iostream>
#include "parser.h"

class BaseFilter {
public:
    BaseFilter() = default;

    virtual void ApplyFilter(BmpHolder &image) = 0;

    virtual ~BaseFilter() = default;
};