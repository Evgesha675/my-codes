package java_course.lab14;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.BorderPane;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class FormattedTextEditor extends Application {

    private TextArea textArea;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Formatted Text Editor");

        BorderPane root = new BorderPane();

        textArea = new TextArea();
        textArea.setFont(Font.font("Arial", 12));
        root.setCenter(textArea);

        MenuBar menuBar = new MenuBar();
        Menu formatMenu = new Menu("Format");
        MenuItem indentMenuItem = new MenuItem("Indent");
        MenuItem unindentMenuItem = new MenuItem("Unindent");

        indentMenuItem.setOnAction(event -> indentText());
        unindentMenuItem.setOnAction(event -> unindentText());

        formatMenu.getItems().addAll(indentMenuItem, unindentMenuItem);
        menuBar.getMenus().add(formatMenu);

        root.setTop(menuBar);

        Scene scene = new Scene(root, 400, 300);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void indentText() {
        String selectedText = textArea.getSelectedText();
        if (selectedText.isEmpty()) {
            return;
        }

        String[] lines = selectedText.split("\n");
        StringBuilder formattedText = new StringBuilder();

        for (String line : lines) {
            formattedText.append("\t").append(line).append("\n");
        }

        int start = textArea.getSelection().getStart();
        int end = textArea.getSelection().getEnd();

        textArea.replaceText(start, end, formattedText.toString());
    }

    private void unindentText() {
        String selectedText = textArea.getSelectedText();
        if (selectedText.isEmpty()) {
            return;
        }

        String[] lines = selectedText.split("\n");
        StringBuilder formattedText = new StringBuilder();

        for (String line : lines) {
            if (line.startsWith("\t")) {
                line = line.substring(1);
            }
            formattedText.append(line).append("\n");
        }

        int start = textArea.getSelection().getStart();
        int end = textArea.getSelection().getEnd();

        textArea.replaceText(start, end, formattedText.toString());
    }
}
