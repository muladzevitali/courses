import { StyleSheet, Image, View, Text, ScrollView, useWindowDimensions, Platform } from "react-native"
import Title from "../components/ui/Title"
import Colors from "../constants/colors"
import PrimaryButton from "../components/ui/PrimaryButton"


const GameOverScreen = ({ enteredNumber, numberOfRounds, onRestart }) => {

    const { width, height } = useWindowDimensions()

    let imageSize = 300;
    if (width < 380) {
        imageSize = 150
    }

    if (height < 400) {
        imageSize = 80
    }

    const imageStyle = {
        width: imageSize,
        height: imageSize,
        borderRadius: imageSize / 2
    }

    return (
        <ScrollView style={styles.screen}>
            <View style={styles.rootContainer}>
                <Title>ყოჩაღ!</Title>
                <View style={[styles.imageContainer, imageStyle]}>
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
        </ScrollView>
    )

}

// const deviceWidth = Dimensions.get('window').width


const styles = StyleSheet.create({
    screen: {
        flex: 1
    },
    rootContainer: {
        flex: 1,
        padding: 24,
        justifyContent: 'center',
        alignItems: 'center'
    },
    imageContainer: {
        // borderRadius: deviceWidth < 380 ? 75 : 175,
        // borderWidth: Platform.OS == 'android' ? 2: 0,
        borderWidth: Platform.select({ios: 0, android: 3}),
        borderColor: Colors.primary800,
        // width: deviceWidth < 380 ? 150 : 300,
        // height: deviceWidth < 380 ? 150 : 300,
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