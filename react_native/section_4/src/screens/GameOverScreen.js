import { StyleSheet, Image, View, Text } from "react-native"
import Title from "../components/ui/Title"
import Colors from "../constants/colors"
import PrimaryButton from "../components/ui/PrimaryButton"


const GameOverScreen = ({enteredNumber, numberOfRounds, onRestart}) => {
    return (
        <View style={styles.rootContainer}>
            <Title>ყოჩაღ!</Title>
            <View style={styles.imageContainer}>
                <Image
                    style={styles.image}
                    source={require('../../assets/images/success.png')}
                />
            </View>
            <Text style={styles.summaryText}>
                შენს ტელეფონს დასჭირდა <Text style={styles.highlight}>{numberOfRounds}</Text> ცდა რომ გამოეცნო რიცხვი <Text style={styles.highlight}>{enteredNumber}</Text>
            </Text>
            <PrimaryButton onPress={onRestart}>თავიდან დაწყება</PrimaryButton>
        </View>
    )

}

const styles = StyleSheet.create({
    rootContainer: {
        flex: 1,
        padding: 24,
        justifyContent: 'center',
        alignItems: 'center'
    },
    imageContainer: {
        borderRadius: 150,
        borderWidth: 3,
        borderColor: Colors.primary800,
        width: 300,
        height: 300,
        overflow: 'hidden',
        margin: 36
    },
    image: {
        width: "100%",
        height: "100%",
    },
    summaryText: {
        fontFamily: 'open-sans',
        fontSize: 24,
        textAlign: 'center',
        marginBottom: 24,
    },
    highlight: {
        fontFamily: 'open-sans-bold',
        color: Colors.primary500
    }
})
export default GameOverScreen