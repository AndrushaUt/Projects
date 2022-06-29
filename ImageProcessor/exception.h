#include <string>

enum class Exception {
    EmptyLine,
    InvalidAmountOfArguments,
    InvalidFilter,
    InvalidFile,
    InvalidTypeOfArgument,
    NoOutputFile,
    WrongOutputFile,
    WrongInputFile,
    InvalidArgument
};

class Message {
public:
    static std::string ExceptMessage(const Exception& status) {
        if (status == Exception::EmptyLine) {
            return "Описание формата аргументов командной строки:\n"
                   "{имя программы} {путь к входному файлу} {путь к выходному файлу} [-{имя фильтра 1} [параметр фильтра 1] [параметр фильтра 2] ...] [-{имя фильтра 2} [параметр фильтра 1] [параметр фильтра 2] ...] ...";
        } else if (status == Exception::InvalidFilter) {
            return "Вы ввели несуществующий фильтр";
        } else if (status == Exception::InvalidAmountOfArguments) {
            return "Для одного из ваших фильтров вы ввели неверное количество параметров";
        } else if (status == Exception::InvalidTypeOfArgument) {
            return "Один из параметров имеет некорректный тип";
        } else if (status == Exception::NoOutputFile) {
            return "Вы не ввели путь выходного файла";
        } else if (status == Exception::WrongOutputFile) {
            return "Вы ввели некорректный путь выходного файла";
        } else if (status == Exception::WrongInputFile) {
            return "Вы ввели некорректный путь входного файла";
        } else if(status == Exception::InvalidFile) {
            return "Возникли какие-то проблемы при чтении файла";
        } else if (status == Exception::InvalidArgument){
            return "Вы ввели неверный аргумент";
        }else {
            return "Trouble";
        }
    }
};
