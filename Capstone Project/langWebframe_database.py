from arango import ArangoClient
import sys

client = ArangoClient()

db = client.db('langWeb', username='root', password='user@1234')

g = db.graph('langWeb')
# vertex collections -> 'lang', 'likes', 'media_type', 'resources', 'quality_of_the_content', 'concepts_well_explained', 'course_depth_and_coverage'
#                                                                               q3                      q1                      q2
# x0 = lang
# x link name
# x1 = link http
# x2 = media type

# Function to add data to the database

# def fun():
#     g.create_vertex_collection('lang')
#     g.create_vertex_collection('media_type')
#     g.create_vertex_collection('resources')
#     g.create_vertex_collection('q1')
#     g.create_vertex_collection('q2')
#     g.create_vertex_collection('q3')

#     g.create_edge_definition(
#         edge_collection='lang_resources',
#         from_vertex_collections=['lang'],
#         to_vertex_collections=['resources']
#     )

#     g.create_edge_definition(
#         edge_collection='resources_media_type',
#         from_vertex_collections=['resources'],
#         to_vertex_collections=['media_type']
#     )

#     g.create_edge_definition(
#         edge_collection='resources_q1',
#         from_vertex_collections=['resources'],
#         to_vertex_collections=['q1']
#     )

#     g.create_edge_definition(
#         edge_collection='resources_q2',
#         from_vertex_collections=['resources'],
#         to_vertex_collections=['q2']
#     )

#     g.create_edge_definition(
#         edge_collection='resources_q3',
#         from_vertex_collections=['resources'],
#         to_vertex_collections=['q3']
#     )

lang = g.vertex_collection('lang')
element = []
main = []

def get_name():
    all_name = [doc['name'] for doc in lang.all()]
    return all_name

def get_icon():
    all_icon = [doc['icon'] for doc in lang.all()]
    return all_icon

def get_db(lan):
    element.clear()
    main.clear()
    lr_edge = g.edge_collection('lang_resources')
    l = lr_edge.edges(f'lang/{lan}', direction='out')['edges']

    s = g.traverse(
        start_vertex= f'lang/{lan}',
        direction='outbound',
        strategy='dfs',
        max_depth=0
    )

    main.append(s['vertices'][0]['icon'])
    main.append(s['vertices'][0]['name'])

    for i in l:
        s = g.traverse(
        start_vertex= i['_to'],
        direction='outbound',
        strategy='dfs')
        list = []
        for line in s['vertices']:
            if 'likes' in line:
                list.append(line['_key'])
                list.append(line['likes'])
            if 'link' in line:
                list.append(line['link'])
            if 'type' in line:
                list.append(line['type'])
            
        
        element.append(list)

# main function to add data to the database

# fun main():

#     x0 = input('Enter the lang\n> ')

#     if not lang.has(x0):
#         xx = input('Enter link for its icon\n> ')
#         lang.insert({
#             '_key' : x0,
#             'name' : x0,
#             'icon' : xx
#         })

#     x = input('Give link a name\n> ')
#     x2 = input('Enter its media type\n> ')

#     resources = g.vertex_collection('resources')
#     if not resources.has(x):
#         x1 = input('Enter its link\n> ')
#         resources.insert({
#             '_key' : x,
#             'link' : x1,
#             'likes' : 0
#         })

#     lang_resources = g.edge_collection('lang_resources')
#     if not lang_resources.has(x0 + '_' + x):
#         lang_resources.insert({
#             '_key' : x0 + '_' + x,
#             '_from' : f'lang/{x0}',
#             '_to' : f'resources/{x}'
#         })

#     media = g.vertex_collection('media_type')
#     if not media.has(f'media_type_{x}'):
#         media.insert({
#             '_key' : f'media_type_{x}',
#             'type' : x2
#         })

#     resources_media_type = g.edge_collection('resources_media_type')
#     if not resources_media_type.has(x + '_' + x2):
#         resources_media_type.insert({
#             '_key' : x + '_' + x2,
#             '_from' : f'resources/{x}',
#             '_to' : f'media_type/media_type_{x}'
#         })

#     q1 = g.vertex_collection('q1')
#     if not q1.has(f'q1_{x}'):
#         q1.insert({
#             '_key' : f'q1_{x}',
#             'likes' : 0
#         })

#     resources_q1 = g.edge_collection('resources_q1')
#     if not resources_q1.has(x + '_q1'):
#         resources_q1.insert({
#             '_key' : x + '_q1',
#             '_from' : f'resources/{x}',
#             '_to' : f'q1/q1_{x}'
#         })

#     q2 = g.vertex_collection('q2')
#     if not q2.has(f'q2_{x}'):
#         q2.insert({
#             '_key' : f'q2_{x}',
#             'likes' : 0
#         })

#     resources_q2 = g.edge_collection('resources_q2')
#     if not resources_q2.has(x + '_q2'):
#         resources_q2.insert({
#             '_key' : x + '_q2',
#             '_from' : f'resources/{x}',
#             '_to' : f'q2/q2_{x}'
#         })

#     q3 = g.vertex_collection('q3')
#     if not q3.has(f'q3_{x}'):
#         q3.insert({
#             '_key' : f'q3_{x}',
#             'likes' : 0
#         })

#     resources_q3 = g.edge_collection('resources_q3')
#     if not resources_q3.has(x + '_q3'):
#         resources_q3.insert({
#             '_key' : x + '_q3',
#             '_from' : f'resources/{x}',
#             '_to' : f'q3/q3_{x}'
#         })

    

    
        

# if __name__ == "__main__":
#     main()
