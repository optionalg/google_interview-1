import java.io.*;
import java.util.*;

class FileObject implements Comparable<FileObject> {
  String line=null;
  BufferedReader br = null;
  double epsilon = 0.00000001;

  public FileObject(String fn) throws IOException {
    br = new BufferedReader(new FileReader(fn));
  }

  public void close() {
    try {
      br.close();
    } catch (IOException ex) {
      ex.printStackTrace();
    } 
  }

  public String getline() {
    return this.line;
  }

  public String readline() {
    try {
      line = br.readLine();
    } catch (IOException ex) {
      line = null;
      ex.printStackTrace();
    } 
    return line;
  }

  @Override
  public int compareTo(FileObject o){
    double d= Double.parseDouble(this.getline()) - Double.parseDouble(o.getline());
    if(d>epsilon) return 1;
    if(d<-epsilon) return -1;
    return 0;
  }
}

public class KWayMerge{
  PriorityQueue<FileObject> pq = null;
  public KWayMerge() {
    pq = new PriorityQueue<FileObject>();
  }
  public void add(FileObject o) {
    String s = o.readline();
    if(s!=null) pq.add(o); 
  }
  public void mergeSort() {
    while(!pq.isEmpty()) {
      FileObject fo = pq.poll();
      System.out.println(fo.getline());
      String s = fo.readline();
      if(s==null) fo.close();//always check when adding to q. adding a null file handle invalidates its compare method
      else pq.add(fo);//add it back to queue 
    }
  }
  public static void createTestFiles(int n) {
    int m = 10;
    for(int i=0;i<n;i++) {
      try {
        PrintWriter bw = new PrintWriter("_tmp_"+i+".txt");
        double min=0;
        for(int j=0;j<m;j++) {
          double r = min+Math.random();
          min = r;
          bw.println(r);
        }
        bw.close();
      } catch (IOException ex) {
        ex.printStackTrace();
      }
    }
  }
  public static void main(String[] args) {
    int n=10;
    createTestFiles(n);
    KWayMerge merger = new KWayMerge();
    for(int i=0;i<n;i++) {
      try {
        merger.add(new FileObject("_tmp_"+i+".txt"));
      } catch (IOException ex) {
        ex.printStackTrace();
      }
    }
    merger.mergeSort();
  }
}
