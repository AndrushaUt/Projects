#include "image.h"
#include <fstream>
#include "iostream"

void Bmp::Read(const std::string &path, BmpHolder &bmp_holder) {
    std::ifstream f;
    f.open(path, std::ios::in | std::ios::binary);
    if (!f.is_open()) {
        throw Exception::WrongInputFile;
    }
    try {
        f.read(reinterpret_cast<char *>(bmp_holder.file_header), SIZE_OF_BMP_HEADER);
        if (f.tellg() != SIZE_OF_BMP_HEADER){
            throw Exception::InvalidFile;
        }
        f.read(reinterpret_cast<char *>(bmp_holder.information_header), SIZE_OF_INFO_HEADER);
        if (f.tellg() != SIZE_OF_BMP_HEADER + SIZE_OF_INFO_HEADER){
            throw Exception::InvalidFile;
        }
    } catch (const std::ios_base::failure& fail){
        std::cout << fail.what() << std::endl;
        throw Exception::InvalidFile;
    }
    int bits[] = {0, 8, 16, 24};
    for (size_t i = 2; i <= 5; i++) {
        bmp_holder.file_size += (bmp_holder.file_header[i] << bits[i - 2]);
        bmp_holder.width += (bmp_holder.information_header[i + 2] << bits[i - 2]);
        bmp_holder.height += (bmp_holder.information_header[i + 6] << bits[i - 2]);
    }
    bmp_holder.colors.resize(bmp_holder.height);
    for (size_t i = 0; i < static_cast<size_t>(bmp_holder.height); i++) {
        bmp_holder.colors[i].resize(bmp_holder.width);
    }
    bmp_holder.padding_amount = ((4 - (bmp_holder.width * 3) % 4) % 4);
    for (size_t i = 0; i < static_cast<size_t>(bmp_holder.height); i++) {
        for (size_t j = 0; j < static_cast<size_t>(bmp_holder.width); j++) {
            unsigned char colors[3];
            f.read(reinterpret_cast<char *>(colors), 3);
            bmp_holder.colors[i][j].red = static_cast<double>(colors[2]) / double(255);
            bmp_holder.colors[i][j].green = static_cast<double>(colors[1]) / double(255);
            bmp_holder.colors[i][j].blue = static_cast<double>(colors[0]) / double(255);
        }
        f.ignore(bmp_holder.padding_amount);
    }
    f.close();
}

void Bmp::Write(const std::string &output, BmpHolder &bmp_holder) {
    std::ofstream f;
    f.open(output, std::ios::out | std::ios::binary);
    if (!f.is_open()) {
        throw Exception::WrongOutputFile;
    }
    unsigned char padding[] = {0};
    f.write(reinterpret_cast<char *>(bmp_holder.file_header), SIZE_OF_BMP_HEADER);
    f.write(reinterpret_cast<char *>(bmp_holder.information_header), SIZE_OF_INFO_HEADER);
    for (size_t i = 0; i < static_cast<size_t>(bmp_holder.height); i++) {
        for (size_t j = 0; j < static_cast<size_t>(bmp_holder.width); j++) {
            unsigned char red = static_cast<unsigned char>(bmp_holder.colors[i][j].red * double(255));
            unsigned char green = static_cast<unsigned char>(bmp_holder.colors[i][j].green * double(255));
            unsigned char blue = static_cast<unsigned char>(bmp_holder.colors[i][j].blue * double(255));
            unsigned char colors[] = {blue, green, red};
            f.write(reinterpret_cast<char *>(colors), 3);
        }
        f.write(reinterpret_cast<char *>(padding), ((4 - (bmp_holder.width * 3) % 4) % 4));
    }
    f.close();
}
