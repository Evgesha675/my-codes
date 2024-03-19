<?php
echo '<pre>';

class Teremok {
    protected $stage = [];
    protected $inhouse = [];

    public function __construct(){
        $this->stage[] = "Теремок стоит на краю поля. В нем жили было дедушка да бабушка. Дедушка умер, бабушка умерла, а мышка от жизни ушла.";
    }

    public function addResident($resident) {
        $this->inhouse[] = $resident;
    }

    public function getResidents() {
        return $this->inhouse;
    }

    public function askWho() {
        $residents = $this->getResidents();
        if (!empty($residents)) {
            return 'В теремочке живут: ' . implode(', ', $residents) . '.';
        } else {
            return 'В теремочке никто не живет.';
        }
    }

    public function render(){
        foreach($this->stage as $stage){
            echo $stage . "<br>";
        }
    }
}

class Animal {
    protected $name;

    public function __construct($name){
        $this->name = $name;
    }

    public function getName() {
        return $this->name;
    }

    public function getIntroduction(){
        return "Пришел " . $this->name . ", увидел теремок и стучится. Спрашивает:";
    }

    public function answer(){
        return "В теремочке живу я, " . $this->name . ".";
    }

    public function action(Teremok $teremok){
        $teremok->addResident($this->getName());
        return $this->name . " прыгнул в теремок и решил остаться жить вместе с другими.";
    }
}

$teremok = new Teremok();

$animals = [
    new Animal('Мышка-Нарушка'),
    new Animal('Лягушка-Квакушка'),
    new Animal('Зайчик-Попрыгайчик'),
    new Animal('Лисичка-Сестричка'),
    new Animal('Волк-Зубами-Щёлк'),
    new Animal('Медведь'),
];

foreach ($animals as $animal) {
    // Introduction
    $teremok->stage[] = $animal->getIntroduction();
    // Answering who the character is
    $teremok->stage[] = $animal->answer();
    // Taking action to move into the Teremok
    $teremok->stage[] = $animal->action($teremok);
}

// Asking who lives in the Teremok
$teremok->stage[] = $teremok->askWho();

// Rendering the stages of the story
$teremok->render();
?>
