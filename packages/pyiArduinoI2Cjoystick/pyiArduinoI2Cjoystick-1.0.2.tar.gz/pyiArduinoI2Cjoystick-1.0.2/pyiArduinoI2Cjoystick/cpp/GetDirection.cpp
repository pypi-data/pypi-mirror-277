// ДАННЫЙ ПРИМЕР ВЫВОДИТ НАПРАВЛЕНИЯ ДЖОЙСТИКА:   // * Строки со звёздочкой являются необязательными.
                                                  //
#include <iostream>
#include <math.h>
#include "../iarduino_I2C_Joystick.h"             //   Подключаем библиотеку для работы с джойстиком I2C-flash.
iarduino_I2C_Joystick joy(0x09);                  //   Объявляем объект joy для работы с функциями и методами библиотеки iarduino_I2C_Joystick, указывая адрес модуля на шине I2C.

class vpadlu {
        public:
                void begin(int) {;};
                template<typename T> void println(T arg)
                {
                        std::cout << arg << '\n' << std::flush;
                }
                template<typename T> void print(T arg)
                {
                        std::cout << arg << std::flush;
                }
                operator bool() { return true; }
} Serial;
                                                  //   Если объявить объект без указания адреса (iarduino_I2C_Joystick joy;), то адрес будет найден автоматически.
int x,y,a;                                        //   Объявляем переменные для получения координат «x»,«y» и рассчёта угла смещения джойстика «a».
                                                  //
void setup(){                                     //
    delay(500);                                   // * Ждём завершение переходных процессов связанных с подачей питания.
    Serial.begin(9600);                           //
    while(!Serial){;}                             // * Ждём завершения инициализации шины UART.
    joy.begin();                                  //   Инициируем работу с джойстиком.
}                                                 //
                                                  //
void loop(){                                      //
    joy.getPosition(x,y);                         //   Получаем координаты в переменные x и y.
    a = atan((float)abs(y)/(float)abs(x))*57.3;   //   Вычисляем угол смещения джойстика от   0° до  90°.
    if( x<0  && y>=0 ){a=180-a;}                  //   Вычисляем угол смещения джойстика от  90° до 180°.
    if( x<0  && y<0  ){a=180+a;}                  //   Вычисляем угол смещения джойстика от 180° до 270°.
    if( x>=0 && y<0  ){a=360-a;}                  //   Вычисляем угол смещения джойстика от 270° до 360°.
//  Выводим направление джойстика:                //
    if( !x && !y ){;}else                         // * Джойстик не смещён.
    if( a <= 15  ){Serial.println( "    X    " ); // * Джойстик смещён вправо.
                   Serial.println( "      X  " ); // * (угол смещения от 0° до 15°)
                   Serial.println( "X X X X X" ); // *
                   Serial.println( "      X  " ); // *
                   Serial.println( "    X    " ); // *
                  }else                           // *
    if( a <= 60  ){Serial.println( "    X X X" ); // * Джойстик смещён вверх и вправо.
                   Serial.println( "      X X" ); // * (угол смещения от 15° до 60°)
                   Serial.println( "    X   X" ); // *
                   Serial.println( "  X      " ); // *
                   Serial.println( "X        " ); // *
                  }else                           // *
    if( a <= 105 ){Serial.println( "    X    " ); // * Джойстик смещён вверх.
                   Serial.println( "  X X X  " ); // * (угол смещения от 60° до 105°)
                   Serial.println( "X   X   X" ); // *
                   Serial.println( "    X    " ); // *
                   Serial.println( "    X    " ); // *
                  }else                           // *
    if( a <= 150 ){Serial.println( "X X X    " ); // * Джойстик смещён вверх и влево.
                   Serial.println( "X X      " ); // * (угол смещения от 105° до 150°)
                   Serial.println( "X   X    " ); // *
                   Serial.println( "      X  " ); // *
                   Serial.println( "        X" ); // *
                  }else                           // *
    if( a <= 195 ){Serial.println( "    X    " ); // * Джойстик смещён влево.
                   Serial.println( "  X      " ); // * (угол смещения от 150° до 195°)
                   Serial.println( "X X X X X" ); // *
                   Serial.println( "  X      " ); // *
                   Serial.println( "    X    " ); // *
                  }else                           // *
    if( a <= 240 ){Serial.println( "        X" ); // * Джойстик смещён вниз и влево.
                   Serial.println( "      X  " ); // * (угол смещения от 195° до 240°)
                   Serial.println( "X   X    " ); // *
                   Serial.println( "X X      " ); // *
                   Serial.println( "X X X    " ); // *
                  }else                           // *
    if( a <= 285 ){Serial.println( "    X    " ); // * Джойстик смещён вниз.
                   Serial.println( "    X    " ); // * (угол смещения от 240° до 285°)
                   Serial.println( "X   X   X" ); // *
                   Serial.println( "  X X X  " ); // *
                   Serial.println( "    X    " ); // *
                  }else                           // *
    if( a <= 330 ){Serial.println( "X        " ); // * Джойстик смещён вниз и вправо.
                   Serial.println( "  X      " ); // * (угол смещения от 285° до 330°)
                   Serial.println( "    X   X" ); // *
                   Serial.println( "      X X" ); // *
                   Serial.println( "    X X X" ); // *
                  }else                           // *
    if( a <= 360 ){Serial.println( "    X    " ); // * Джойстик смещён вправо.
                   Serial.println( "      X  " ); // * (угол смещения от 330° до 360°)
                   Serial.println( "X X X X X" ); // *
                   Serial.println( "      X  " ); // *
                   Serial.println( "    X    " ); // *
                  }                               // *
    if(  x || y  ){Serial.println( "\r\n\r\n" );} // * Если джойстик смещён, то добавляем три пустые строки.
    delay(200);                                   // *
}                                                 //

int main()
{
	setup();
	for (;;) {
		loop();
	}
}
