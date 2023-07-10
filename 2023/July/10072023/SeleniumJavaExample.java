import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class SeleniumJavaExample {
    public static void main(String[] args) throws InterruptedException {
        // Set the path to the chromedriver executable
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");

        // Create a new instance of the ChromeDriver
        WebDriver driver = new ChromeDriver();

        // Maximize the browser window
        driver.manage().window().maximize();

        // Navigate to the webpage
        driver.get("https://demostore.x-cart.com/");

        // Find and click on the currency element
        WebElement currency = driver.findElement(By.xpath("//*[@id=\"header-bar\"]/div[2]/a"));
        currency.click();

        // Find the dropdown element and create a Select object
        WebElement dropdownElement = driver.findElement(By.xpath("//*[@id=\"currency_code_1\"]"));
        Select dropdown = new Select(dropdownElement);

        // Get the text of the first selected option
        String text = dropdown.getFirstSelectedOption().getText();
        System.out.println(text);

        // Assert the text is "US Dollar"
        assert text.equals("US Dollar");

        // Pause the execution for 3 seconds (optional)
        Thread.sleep(3000);

        // Close the browser
        driver.quit();
    }
}
