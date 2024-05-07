import { Text, View, Pressable, StyleSheet } from "react-native";
import Colors from "../../constants/colors";

const PrimaryButton = ({ children, onPress }) => {
    return (

        <View style={styles.buttonOuterContainer}>
            <Pressable
                style={({ pressed }) => pressed
                    ? [styles.buttonInnerContainer, styles.presssed]
                    : styles.buttonInnerContainer
                }
                onPress={onPress}
            //android_ripple={{ color: '#640233' }} // android

            >
                <Text style={styles.buttonText}>{children}</Text>
            </Pressable>
        </View >
    )
}

const styles = StyleSheet.create({
    buttonOuterContainer: {
        borderRadius: 28,
        margin: 4,
        overflow: 'hidden'
    },
    buttonInnerContainer: {
        backgroundColor: Colors.primary500,
        paddingVertical: 8,
        paddingHorizontal: 16,
        elevation: 2
    },
    buttonText: {
        color: 'white',
        textAlign: 'center'
    },
    presssed: {
        opacity: .75,
    }
})

export default PrimaryButton;