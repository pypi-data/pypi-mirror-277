// ДАННЫЙ ПРИМЕР ВЫПОЛНЯЕТ КАЛИБРОВКУ ДЖОЙСТИКА:                                  // * Строки со звёздочкой являются необязательными.
                                                                                  //
#include <ncurses.h>
#include <iostream>
#include "Includes/WString.h"
#include "../iarduino_I2C_Joystick.h"                                             //   Подключаем библиотеку для работы с джойстиком I2C-flash.
iarduino_I2C_Joystick joy(0x09);                                                  //   Объявляем объект joy для работы с функциями и методами библиотеки iarduino_I2C_Joystick, указывая адрес модуля на шине I2C.
                                                                                  //   Если объявить объект без указания адреса (iarduino_I2C_Joystick joy;), то адрес будет найден автоматически.
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

unsigned long start;

unsigned long nillis()
{
        return millis() - start;
}

uint32_t tmrStop;                                                                 //
long x, adc_X_min=4096, adc_X_cen=0, adc_X_max=0;                                 //
long y, adc_Y_min=4096, adc_Y_cen=0, adc_Y_max=0;                                 //
                                                                                  //
void setup(){                                                                     //
    delay(500);                                                                   // * Ждём завершение переходных процессов связанных с подачей питания.
    Serial.begin(9600);                                                           //
    while(!Serial){;}                                                             // * Ждём завершения инициализации шины UART.
    joy.begin();                                                                  //   Инициируем работу с джойстиком.
    joy.setAveraging(2);                                                          //   Устанавливаем незначительное усреднение показаний АЦП.
    joy.setDeadZone(7.0);                                                         //   Устанавливаем мёртвую зону центрального положения в 7%.
//  Готовимся определить центральное положение джойстика:                         //
    Serial.println(  ("\r\nКАЛИБРОВКА ДЖОЙСТИКА:\r\n")                         ); //
    Serial.println(  ("Отпустите джойстик.")                                   ); //
    Serial.println(  ("Он должен самостоятельно установиться")                 ); //
    Serial.println(  ("в центральное положение.")                              ); //
    Serial.print  (  ("Ждём.")                                                 ); //
    for(int i=0; i<5; i++){ delay(1000); Serial.print("."); }                     //   Даём время пользователю отпустить джойстик.
//  Получаем значения АЦП соответствующие центральному положению:                 //
    for(int i=0; i<10; i++){                                                      //   Выполняем цикл чтения 10 раз.
        joy.getADC(x,y); std::cout<<"\r\nАЦП = "<<x<<":"<<y<<std::flush;          //   Получаем текущие значения АЦП в указанные переменные.
        adc_X_cen += x;  adc_Y_cen += y; delay(200);                              //   Получаем АЦП центра, прибавляя его к предыдущему значению.
    }   adc_X_cen /= 10; adc_Y_cen /= 10;                                         //   Получаем среднее арифметическое значение АЦП центра.
//  Готовимся определить крайние положения джойстика:                             //
    Serial.println(  ("\r\nГотово!") );                                           //
    Serial.println(  ("------------------------------------------------")      ); //
    Serial.println( ""                                                         ); //
    Serial.println(  ("Теперь медленно поворачивайте джойстик по кругу,")      ); //
    Serial.println(  ("со скоростью 1 полный оборот за 2-3 секунды,")          ); //
    Serial.println(  ("на максимальном удалении джойстика от центра.")         ); //
//  Получаем значения АЦП соответствующие крайним положениям:                     //
    tmrStop = nillis() + 10000;                                                   //   Определяем время завершения снятия показаний.
    while(nillis()<tmrStop){                                                      //   Выполняем цикл пока не достигнем времени tmrStop...
        joy.getADC(x,y);                                                          //   Получаем текущие значения АЦП в указанные переменные.
        if( x < adc_X_min ){ adc_X_min = x; }                                     //   Получаем минимальное  значение АЦП по оси X.
        if( y < adc_Y_min ){ adc_Y_min = y; }                                     //   Получаем минимальное  значение АЦП по оси Y.
        if( x > adc_X_max ){ adc_X_max = x; }                                     //   Получаем максимальное значение АЦП по оси X.
        if( y > adc_Y_max ){ adc_Y_max = y; }                                     //   Получаем максимальное значение АЦП по оси Y.
        if(nillis()%1000<10){ delay(10); Serial.print("."); }                     //   Выводим точку в монитор, один раз в секунду.
    }                                                                             //
//  Выводим результат:                                                            //
    Serial.println(  ("\r\nГотово!")                                           ); //
    Serial.println(  ("------------------------------------------------")      ); //
    Serial.println( ""                                                         ); //
    Serial.print( "АЦП по оси X меняется от ");
    Serial.print(adc_X_min);
    Serial.print(" до ");
    Serial.print(adc_X_max);
    Serial.print(", с центром в ");
    Serial.println(adc_X_cen);
    Serial.print( "АЦП по оси Y меняется от ");
    Serial.print(adc_Y_min);
    Serial.print(" до ");
    Serial.print(adc_Y_max);
    Serial.print(", с центром в ");
    Serial.println(adc_Y_cen);
    Serial.println(  ("================================================")      ); //
    Serial.println( ""                                                         ); //
//  Калибруем джойстик (данные сохранятся в его flash памяти):                    //
    joy.setCalibration_X(adc_X_min, adc_X_cen, adc_X_max);                        //  Калибруем координаты по оси X.
    joy.setCalibration_Y(adc_Y_min, adc_Y_cen, adc_Y_max);                        //  Калибруем координаты по оси Y.
//  Готовимся к выводу координат после калибровки:                                //
    Serial.println(  ("\r\nВыводим координаты: для выхода нажмите <ctrl+c>")   ); //
}                                                                                 //
                                                                                  //
void loop(){                                                                      //
                                                                                  //
    joy.getPosition(x,y);                                                         //   Выводим координаты X:Y.
}

int main()
{
        start = millis();
        setup();
        for (;;) {
                loop();
                clrtoeol();
                std::cout << "                                                         " <<'\r' << std::flush;
                std::cout << x << '\t' << y << '\r' << std::flush;
                delay(1);
        }
}
