<?php
// echo "classes";
class A{
    public $a;
    private $b=true;
    protected $c = 43;
}
class B extends A{
    protected $c = 'world';
    public function doSmth(){
        echo $this->c;
    }
}
class User{
    public $name;
    public $secondname;
    public $city = 'Irkutsk';
    public function _construct($name = null){
        $this->name = $name;
        $this->secondname = 'Kik';
    }
    public function sayHello ()  {
        echo "Hello, i'm" , $this ->name;
        echo PHP_EOL;
        
    }
}

$user = new User;
$mary = new User('Mary');
$user->sayHello();

print_r($user);//тоже отладка?

$a = new A;
$a = new B;
$a -> doSmth();
$a->a = 'Hello';

var_dump($a); //для отладки 

