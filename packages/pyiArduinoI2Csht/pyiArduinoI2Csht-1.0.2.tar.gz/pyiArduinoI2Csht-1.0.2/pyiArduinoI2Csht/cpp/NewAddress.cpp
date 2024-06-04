// Данный пример меняет адрес модуля на указанный в argv[1].

#include <iostream>
#include "../iarduino_I2C_SHT.h"

iarduino_I2C_SHT sht;

uint8_t newAddress = 9;

int main(int argc, char** argv){
        if (argc > 1) {

                newAddress = atoi(argv[1]);

        }

        if (sht.begin()){

                std::cout << "На шине I2C найден модуль с адресом 0x";
                std::cout << std::hex << int(sht.getAddress());
                std::cout << " который является расширителем выводов\n";

                if (sht.changeAddress(newAddress)){

                        std::cout << "Адрес модуля изменён на 0x";
                        std::cout << std::hex << int(sht.getAddress()) << '\n';
                }
                else {

                        std::cout << "Адрес модуля изменить не удалось!" << '\n';

                }
        }
        else {

                std::cout << "Расширитель выводов не найден!" << '\n';

        }
}

//  ПРИМЕЧАНИЕ:
//  Данная программа демонстрирует не только возможность смены адреса
//  на указанный в переменной newAddress, но и обнаружение, и вывод
//  текущего адреса модуля на шине I2C.
