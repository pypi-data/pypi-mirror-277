// ПРИМЕР ЧТЕНИЯ ВСЕХ ЗНАЧЕНИЙ ПРИ ИХ ИЗМЕНЕНИИ:

#include <iostream>
#include "../iarduino_I2C_SHT.h"

iarduino_I2C_SHT sht;

void loop(void);

int main()
{
        sht.begin();
        sht.setTemChange(0.1);
        sht.setHumChange(1.0);

        while(1) {
                loop();
        }
}

void loop()
{

        if (sht.getTemChanged()) {
                std::cout << ("Температура = ");
                std::cout << ( sht.getTem() );
                std::cout << (" °С.\r\n");
        }

        if (sht.getHumChanged()) {
                std::cout << ("Влажность = ");
                std::cout << ( sht.getHum() );
                std::cout << (" %.\r\n");
        }
}
