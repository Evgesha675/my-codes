// package java_course;

// public class Car {

//     private String make;

//     private String model;

//     private int year;

//     private boolean headlightsOn;

    

//     public Car(String make, String model, int year) {

//         this.make = make;

//         this.model = model;

//         this.year = year;

//     }

    

//     public Car(String make, String model, int year, boolean headlightsOn) {

//         this.make = make;

//         this.model = model;

//         this.year = year;

//         this.headlightsOn = headlightsOn;

//     }

    

//     public void turnOnHeadlights() {

//         this.headlightsOn = true;

//         System.out.println("Headlights are now turned on.");

//     }

    

//     public void turnOnHeadlights(int brightnessLevel) {

//         this.headlightsOn = true;

//         System.out.println("Headlights are now turned on to brightness level " + brightnessLevel + ".");

//     }

    

//     public static void main(String[] args) {

//         Car car1 = new Car("Honda", "Civic", 2022, false);

//         car1.turnOnHeadlights();

        

//         Car car2 = new Car("Toyota", "Corolla", 2022);

//         car2.turnOnHeadlights(5);

//     }

// }
