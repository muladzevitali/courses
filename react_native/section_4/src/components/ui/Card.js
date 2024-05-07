import {View, StyleSheet} from 'react-native'
import Colors from '../../constants/colors'

const Card = ({children}) => {
    return (
        <View style={styles.card}>
                {children}
            </View>
    )
}

const styles = StyleSheet.create({
    card: {
        justifyContent: 'space-between',
        alignItems: 'center',
        marginTop: 36,
        marginHorizontal: 24,
        padding: 16,
        backgroundColor: Colors.primary800,
        borderRadius: 8,
        elevation: 4, // android
        shadowColor: 'black', //  iOS
        shadowOffset: { width: 0, height: 2 }, // iOS
        shadowRadius: 6 // iOS
    }
})

export default Card;