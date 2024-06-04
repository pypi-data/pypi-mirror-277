// ПРИМЕР ЧТЕНИЯ ВСЕХ ЗНАЧЕНИЙ ДАТЧИКА:

#include <iostream>
#include "../iarduino_I2C_SHT.h"

iarduino_I2C_SHT sht;

void loop(void);

int main()
{
        sht.begin();
        while(1) {
                loop();
        }
}

void loop()
{
        std::cout << "Температура = ";
        std::cout <<  sht.getTem();
        std::cout << " °C, влажность = ";
        std::cout <<  sht.getHum();
        std::cout << " %.\r\n";
        delay(500);
}
