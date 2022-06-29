
const int SIZE_OF_BMP_HEADER = 14;
const int SIZE_OF_INFO_HEADER = 40;

struct BmpHolder {
    unsigned char file_header[SIZE_OF_BMP_HEADER];
    unsigned char information_header[SIZE_OF_INFO_HEADER];
    int file_size = 0;
    int width = 0;
    int height = 0;
    std::vector<std::vector<Color>> colors;
    size_t padding_amount;
    std::string input_file;
    std::string output_file;
};