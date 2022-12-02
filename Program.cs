namespace adventofcode {
  public class Program {
    public const string WorkingDir = "D:/repos/AdventOfCode22";
    public static void Main() {
      Console.WriteLine("Test output 2");
      Day01.Run();
    }

    public static string GetInputPath(string input, string day) {
      return Path.Join(WorkingDir, day, input);
    }
  }
}