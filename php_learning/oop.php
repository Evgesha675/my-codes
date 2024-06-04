 <?php
/* class User
// {


 } */
// $user = new User; //объект

// class B extends User
// {
//     //B с наследованием User
// }
// private protected public 
// public $prop;//переменная без значения
// $obj->prop // обращение к свойствам 
// let obj = {};
// obj.prop;
// obj['prop'];

//переопределили переменую (зачем?)
class A{
    const MY_CONST = 42;
    public static $prop = 42;
    public static function DoSmth(){
        echo self::MY_CONST; //при self наследование не идёт (при static всё будет наследовано) и при self не важно название класса
    }
}
class B extends A{
    const MY_CONST = 43;
}
$c = new B;
echo A::MY_CONST;//обращение к константе
echo "\n";
echo B::MY_CONST;
echo "\n";
echo A::$prop;//обращение к статике(к свойству)
echo "\n";

A::DoSmth();
B::DoSmth();//опа, а не наследовалось

// имена классов в PascalCase

// конструткоры и деструкторы есть (пример не записал)

// есть пространтсва имён для изолирования 
/* namespace App;
class User{}
$user = new \App\User('Name'); 
*/

// абстрактные классы
/*abstract class Model
{abstract public function action();
}
class User extends Model{
    public function action(){
        //реализация метода
    }
} */

//интерфейсы используются для указание того, какие методы должен реализовывать классы
/*
interface Storage{
    public function getItem($name,$value);
    public function getItem($name);
}
class Disk implements Storage{ 
    public function setItem($name,$value){
        //реализация
    }
    public function getItem($name){
        //реализация
    }
}*/
//для разграничения класса и интерфейса обзывают постфикс Contract или префикс I (1)

//Трейты - механизм повторного использования кода, дополнение к обычному наследованию класса
/*
trait SaysHello{
    public function sayHello(){
        echo 'Hello';
    }
}
class User{
    use SaysHello;
    //у класса user теперь есть метод sayHello
} */

// у всего этого по дефолту одно пространство имён (см. (1))