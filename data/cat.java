package data;
public class cat {
    private int talelen;
    private String name;
    
    public cat(int talelen, String name){
        this.talelen = talelen;
        this.name=name;
    }
    public cat(){
        this(30,"Tom");
    }
    
    public int gettale(){
        return talelen;
    }
    public String getName(){
        return name;
    }
    @Override
    public boolean equals(Object obj){
        cat tmp = (cat)obj;
        return (this.gettale()==tmp.gettale())&&(this.getName().equals(tmp.getName()));
    }
}
