public class Data {
    public int pub_v;
    private int pv_v;
    public static int count = 2;
    private int default_value; // This default value should be 0

    public Data() {
        pub_v = 99;
        pv_v = 199;
    }

    public int get_v() {
        return pv_v;
    }

    public void set_v(int v) {
        pv_v = v;
    }

    public void increment()
    {
        count++;
    }

    public int get_default_v() {return default_value;}

}
