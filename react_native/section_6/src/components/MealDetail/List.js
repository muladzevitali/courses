import { View, Text, StyleSheet } from 'react-native'

const List = ({ data }) => {
    return (
        data.map(dataPoint => (
            <View key={dataPoint} style={styles.listItem}>
                <Text style={styles.itemText}>{dataPoint}</Text>
            </View>
        ))
    )
}

const styles = StyleSheet.create({
    listItem: {
        borderRadius: 6,
        paddingHorizontal: 8,
        paddingVertical: 4,
        marginVertical: 4,
        marginHorizontal: 12,
        backgroundColor: '#3f2f25'
    },
    itemText: {
        color: 'white',
        textAlign: 'center'
    }
})

export default List