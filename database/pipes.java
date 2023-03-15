package database;

public class pipes {
    private int id;
    private String pipes_length;
    private String pipes_diameter;
    private String pipes_wall_thickness;

    public pipes(){
        this.id = id;
        this.pipes_length = pipes_length;
        this.pipes_diameter = pipes_diameter;
        this.pipes_wall_thickness = pipes_wall_thickness;
    }

    public static void add(String s) {
    }

    public int getId(){return id;}
    public void setId(int id){
        this.id=id;
    }
    public String getPipes_length(){return pipes_length;}

    public String setPipes_length(String pipes_length) {
        this.pipes_length = pipes_length;
        return pipes_length;
    }
    public  String getPipes_diameter(){return pipes_diameter;}

    public String setPipes_diameter(String pipes_diameter) {
        this.pipes_diameter = pipes_diameter;
        return pipes_diameter;
    }

    public String getPipes_wall_thickness() {
        return pipes_wall_thickness;
    }

    public String setPipes_wall_thickness(String pipes_wall_thickness) {
        this.pipes_wall_thickness = pipes_wall_thickness;
        return pipes_wall_thickness;
    }

    @Override
    public String toString() {
        return "pipes{" +
                "id=" + id +
                ", pipes_length='" + pipes_length + '\'' +
                ", pipes_diameter='" + pipes_diameter + '\'' +
                ", pipes_wall_thickness='" + pipes_wall_thickness + '\'' +
                '}';
    }
}