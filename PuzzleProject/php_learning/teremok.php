<?php
echo '<pre>';
/*
-Мышка-Нарушка
-Лягушка-Квакушка
-Зайчик-Попрыгайчик
-Лисичка-Сестричка
-Волк-Зубами-Щёлк
-Медведь
*/
class Teremok {
    protected $stage = [];
    protected $inhouse = [];
    public function __consruct(){

    }
    public function render(){
        foreach($this->names as $stage){
            echo $stage = new Instruction();
        }
    }
}

class Mouse{
    public $name  = 'Мышка-Нарушка';
    public function  getIntroduction(){
        return "Бежала " . $this->name . "Увидала теремок, стучится и спрашивает.";
    }
    public function askWho(){
        return 'Кто-кто в теремочке живёт?';
    }
    public function answer(){
        return "Я" . $this->name;
    }

    public function action(){
        return $this->name . "запрыгивай в теремок, будем жить вместе";
    }
}


class Stage {

}

class Mouse extends Stage{
    
}