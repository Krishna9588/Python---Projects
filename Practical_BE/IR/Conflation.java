import java.util.*; [cite: 2]
import java.util.InputMismatchException; // Added for clarity, though covered by util.*

public class Conflation { [cite: 3]
    private static List<String> textList = new ArrayList<>(); [cite: 4]
    private static Scanner scanner = new Scanner(System.in); [cite: 5]

    public static void main(String[] args) { [cite: 6]
        // Initialize with sample text
        textList = new ArrayList<>(Arrays.asList("she", "went", "to", "the", "store", "and", "bought", "fruits")); [cite: 8]
        int choice = 0; [cite: 9, 43]

        do { [cite: 10]
            System.out.println("\nText Processing Menu:"); [cite: 11]
            System.out.println("1. Display text"); [cite: 12]
            System.out.println("2. Remove punctuation and stop words"); [cite: 13]
            System.out.println("3. Suffix stripping"); [cite: 14]
            System.out.println("4. Count word frequency"); [cite: 15]
            System.out.println("5. Exit"); [cite: 16]
            System.out.print("Enter your choice: "); [cite: 17]

            try { [cite: 18]
                choice = scanner.nextInt(); [cite: 19]
                scanner.nextLine(); // Consume newline [cite: 20]

                switch (choice) { [cite: 21]
                    case 1:
                        displayText(); [cite: 23]
                        break;
                    case 2:
                        removePunctuationAndStopWords(); [cite: 26] // Fixed method name
                        break;
                    case 3:
                        suffixStripping(); [cite: 29]
                        break;
                    case 4:
                        countFrequency(); [cite: 32]
                        break;
                    case 5:
                        System.out.println("Exiting program..."); [cite: 35]
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again."); [cite: 38]
                } [cite: 39]
            } catch (InputMismatchException e) { [cite: 40] // Fixed exception name
                System.out.println("Invalid input. Please enter a number."); [cite: 41]
                scanner.nextLine(); // Clear the invalid input [cite: 42]
                choice = 0; // Continue the loop [cite: 43]
            }
        } while (choice != 5); [cite: 45] // Fixed comparison operator

        scanner.close(); [cite: 47]
    } [cite: 46]

    private static void displayText() { [cite: 48]
        System.out.println("Current text:"); [cite: 49]
        for (String word : textList) { [cite: 50]
            System.out.print(word + " "); [cite: 51]
        }
        System.out.println(); [cite: 54]
    }

    private static void removePunctuationAndStopWords() { [cite: 55] // Fixed method name
        List<String> stopWords = Arrays.asList("a", "an", "the", "and", "or", "but"); [cite: 57]
        List<String> processedText = new ArrayList<>(); [cite: 58]

        for (String word : textList) { [cite: 59]
            // Remove punctuation and make lowercase [cite: 61]
            String cleanWord = word.replaceAll("[^a-zA-Z]", "").toLowerCase();

            // Check if it's not a stop word (moved this block inside the loop)
            if (!stopWords.contains(cleanWord) && !cleanWord.isEmpty()) { [cite: 64]
                processedText.add(cleanWord); [cite: 65]
            }
        } [cite: 62, 66] // Fixed bracket placement

        textList = processedText; [cite: 68]
        System.out.println("Punctuation and stop words removed."); [cite: 69]
        displayText(); [cite: 70]
    }

    private static void suffixStripping() { [cite: 71]
        List<String> processedText = new ArrayList<>(); [cite: 73]
        for (String word : textList) { [cite: 74]
            String strippedWord = word; [cite: 75]
            String[] suffixes = {"ing", "ed", "er", "est", "ly", "tion", "ness"}; [cite: 77]

            for (String suffix : suffixes) { [cite: 78]
                if (strippedWord.endsWith(suffix) && strippedWord.length() > suffix.length()) { [cite: 79]
                    strippedWord = strippedWord.substring(0, strippedWord.length() - suffix.length()); [cite: 80, 81]
                    break; // Only strip one suffix (moved inside if-block) [cite: 83]
                } [cite: 82]
            } [cite: 84]
            processedText.add(strippedWord); [cite: 86]
        } [cite: 85]

        textList = processedText; [cite: 88]
        System.out.println("Suffixes stripped."); [cite: 89]
        displayText(); [cite: 90]
    }

    private static void countFrequency() { [cite: 91]
        Map<String, Integer> frequencyMap = new HashMap<>(); [cite: 93]

        for (String word : textList) { [cite: 94]
            // Moved this line inside the loop
            frequencyMap.put(word, frequencyMap.getOrDefault(word, 0) + 1); [cite: 96]
        } [cite: 95] // Fixed bracket placement

        System.out.println("Word frequency:"); [cite: 97]
        for (Map.Entry<String, Integer> entry : frequencyMap.entrySet()) { [cite: 98]
            System.out.println(entry.getKey() + ":" + entry.getValue()); [cite: 99]
        } [cite: 100]
    }
} [cite: 102]