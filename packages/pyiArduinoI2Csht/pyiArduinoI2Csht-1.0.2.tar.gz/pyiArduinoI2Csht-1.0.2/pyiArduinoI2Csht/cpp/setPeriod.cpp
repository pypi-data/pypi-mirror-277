// ЗАДАНИЕ ПЕРИОДА ОБНОВЛЕНИЯ ПОКАЗАНИЙ ДАТЧИКОВ:

#include <iostream>
#include "../iarduino_I2C_SHT.h"

iarduino_I2C_SHT sht;

void loop(void);

int main()
{

        sht.begin();
        sht.setPeriod(2.0);
        while(1) {

                loop();

        }

}

void loop()
{

        std::cout << "t=" << sht.getTem() << "°C, ";
        std::cout << "RH=" << sht.getHum() << "%\n";
        delay(100);

}
