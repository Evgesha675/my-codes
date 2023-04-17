package databasenew;

public class Pipe {
    private int id;
    private double length;
    private double width;
    private int walls;

    public Pipe(int id, double length, double width, int walls) {
        this.id = id;
        this.length = length;
        this.width = width;
        this.walls = walls;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public int getWalls() {
        return walls;
    }

    public void setWalls(int walls) {
        this.walls = walls;
    }

    @Override
    public String toString() {
        return "Pipe{" +
                "id=" + id +
                ", length=" + length +
                ", width=" + width +
                ", walls=" + walls +
                '}';
    }
}
