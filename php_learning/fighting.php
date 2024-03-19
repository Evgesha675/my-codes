<?php

// Базовый класс для персонажей
class Character {
    protected $name;
    protected $health;

    public function __construct($name, $health) {
        $this->name = $name;
        $this->health = $health;
    }

    public function getName() {
        return $this->name;
    }

    public function getHealth() {
        return $this->health;
    }

    // Метод для атаки
    public function attack($target) {
        $damage = mt_rand(5, 20); // Случайное значение урона
        echo "{$this->name} атаковал {$target->getName()} и нанес {$damage} урона. \n";
        $target->takeDamage($damage);
    }

    // Метод для получения урона
    public function takeDamage($damage) {
        $this->health -= $damage;
        echo "{$this->name} получил {$damage} урона. \n";
    }
}

// Интерфейс для бойцов
interface Fighter {
    public function fight();
}

// Трейт для дополнительных возможностей
trait AdditionalAbilities {
    public function useSpecialAbility() {
        echo "{$this->name} использовал(а) специальную способность!\n";
    }
}

// Класс для игрока
class Player extends Character {
    use AdditionalAbilities;

    public function __construct($name, $health) {
        parent::__construct($name, $health);
    }
}

// Класс для роботов
class Robot extends Character implements Fighter {
    private $energy;

    public function __construct($name, $health, $energy) {
        parent::__construct($name, $health);
        $this->energy = $energy;
    }

    public function getEnergy() {
        return $this->energy;
    }

    // Реализация метода атаки
    public function attack($target) {
        $damage = $this->fight(); // Вызываем метод fight() для нанесения урона и использования энергии
        echo "{$this->name} атаковал {$target->getName()} и нанес {$damage} урона. \n";
        $target->takeDamage($damage);
    }

    // Реализация метода из интерфейса
    public function fight() {
        $damage = mt_rand(10, 30); // Случайное значение урона во время сражения
        $this->useEnergy();
        return $damage;
    }

    // Метод для использования энергии
    private function useEnergy() {
        $use_energy = mt_rand(10,30); // Случайное значение потери энергии для робота
        $this->energy -= $use_energy;
    }
}

// Создание экземпляров классов и их использование
$player = new Player("Игрок", 100);
$robot = new Robot("Робот", 150, 50);

$player->attack($robot);
$robot->attack($player);

$player->useSpecialAbility();

echo "{$player->getName()} имеет {$player->getHealth()} здоровья.\n";
echo "{$robot->getName()} имеет {$robot->getHealth()} здоровья и {$robot->getEnergy()} енергии.\n";

?>
