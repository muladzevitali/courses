import { View, Text, StyleSheet } from 'react-native'
import { GlobalStyles } from '../../constants/styles'
import Button from './Button'


const ErrorOverlay = ({ message, onConfirm }) => {
    return (
        <View style={styles.container}>
            <Text style={[styles.text, styles.title]}> Error ocurred</Text>
            <Text style={[styles.text, styles.message]}> {message}</Text>
            <Button onPress={onConfirm}>Okay</Button>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 24,
        backgroundColor: GlobalStyles.colors.primary700
    },
    text: {
        textAlign: 'center',
        marginBottom: 8,
        color: 'white'
    },
    title: {
        fontSize: 20,
        fontWeight: 'bold'
    },
    message: {
        fontSize: 14
    }
})

export default ErrorOverlay