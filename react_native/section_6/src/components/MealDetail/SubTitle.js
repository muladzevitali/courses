import { View, Text, StyleSheet } from 'react-native'

const SubTitle = ({ children }) => {
    return (
        <View style={styles.subTitleContainer}>
            <Text style={styles.subTitle}>{children}</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    subTitleContainer: {
        borderBottomColor: '#e2b497',
        borderBottomWidth: 2,
        padding: 6,
        marginHorizontal: 12,
        marginVertical: 4
    },
    subTitle: {
        fontSize: 18,
        fontWeight: 'bold',
        textAlign: 'center',
        color: '#3f2f25'
    }
})

export default SubTitle