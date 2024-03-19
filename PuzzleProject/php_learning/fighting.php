<?php
// Базовый класс для персонажей
class Character {
    protected $name;
    private $health;

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

    public function setHealth($health) {
        $this->health = $health;
    }

    // Метод для атаки
    public function attack($target) {
        $damage = mt_rand(5, 20); // Случайное значение урона
        $target->takeDamage($damage);
        echo "{$this->name} атаковал {$target->getName()} и нанес {$damage} урона. \n";
    }

    // Метод для получения урона
    protected function takeDamage($damage) {
        $this->health -= $damage;
        echo "{$this->name} получил {$damage} урона. \n";
    }
}

// Унаследованный класс для роботов
class Robot extends Character implements Fighter {
    private $energy;

    public function __construct($name, $health, $energy) {
        parent::__construct($name, $health);
        $this->energy = $energy;
    }

    public function getEnergy() {
        return $this->energy;
    }

    public function useEnergy() {
        $this->energy -= 10;
    }

    // Реализация метода из интерфейса
    public function fight() {
        $this->useEnergy();
        return mt_rand(10, 30); // Случайное значение урона во время сражения
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

// Создание экземпляров классов и их использование
$player = new Player("Игрок", 100);
$robot = new Robot("Робот", 150, 50);

$player->attack($robot);
$robot->attack($player);

$player->useSpecialAbility();

echo "{$player->getName()} имеет {$player->getHealth()} здоровья.\n";
echo "{$robot->getName()} имеет {$robot->getHealth()} здоровья и {$robot->getEnergy()} енергии.\n";
