<template>
    <v-container>
        <v-card
        class="mx-2"
        color="#303030"
        dark
        max-width="400"
        >
            <v-card-title>
            <!-- <v-icon
                large
                left
            >
                mdi-twitter
            </v-icon> -->
            <span class="title font-weight-light">Comment</span>
            </v-card-title>

            <v-card-text class="headline font-weight-bold">
            <!-- {{comment_object}} -->
            <v-col cols="12" md="10">
                <v-textarea
                    v-show="$store.state.role === 'reviewer' && $store.state.id === comment_object.Writer && !comment_object.Submited"
                    outlined
                    name="input-7-4"
                    label="Text Area"
                    v-model="comment_object.Context"
            ></v-textarea>
                            <v-textarea
                    v-show="$store.state.role === 'reviewer' && $store.state.id === comment_object.Writer && comment_object.Submited"
                    outlined
                    name="input-7-4"
                    label="Text Area"
                    v-model="comment_object.Context"
            ></v-textarea>

                </v-col>
                <v-row 
                    v-show="$store.state.role === 'reviewer' && $store.state.id === comment_object.Writer && !comment_object.Submited"    
                    align="center"
                    justify="start">
                    <v-btn class="ml-7 mb-10" color="green lighten-1" @click="pass_fail=1">
                        Pass
                    </v-btn>
                    <v-btn class="ml-3 mb-10" color="red lighten-2" @click="pass_fail=0">
                        Fail
                    </v-btn>    
                </v-row>
                <v-row
                    v-show="$store.state.role === 'reviewer' && $store.state.id === comment_object.Writer && !comment_object.Submited"    
                    align="center"
                    justify="end"
                    >
                    <v-btn class="ma-5" outlined color="blue lighten-2" @click="submitComment">
                        submit
                    </v-btn>
                </v-row>
            </v-card-text>

            <v-card-actions>
            <v-list-item class="grow">
                <v-list-item-avatar color="grey darken-3">
                <v-img
                    class="elevation-6"
                    src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                ></v-img>
                </v-list-item-avatar>

                <v-list-item-content>
                <v-list-item-title>Anonymous</v-list-item-title>
                </v-list-item-content>

                <!-- <v-row
                align="center"
                justify="end"
                >
                <v-icon class="mr-1">mdi-heart</v-icon>
                <span class="subheading mr-2">256</span>
                <span class="mr-1">·</span>
                <v-icon class="mr-1">mdi-share-variant</v-icon>
                <span class="subheading">45</span>
                </v-row> -->
            </v-list-item>
            </v-card-actions>
        </v-card>
    </v-container>
</template>
<script>
export default {
    props: {
        comment_object: Object
    },
    components: {},
    data: () => ({
        pass_fail: -1
    }),
    asyncComputed: {

    },
    computed: {
    },
    methods: {
        async updateComment() {
            try {
                    const that = this
                    const res = await this.$http.put(
                        '/escBackend/comment/'+this.comment_object.id + '/',
                        {
                            Stage: 1,
                            Writer: 1,
                            Context: that.comment_object.Context,
                            Pass_Fail: that.pass_fail,
                            Submited: false
                        }
                    );
                    // location.reload();

                    return res.data.results
            }catch(e) {
                window.console.log(e);
            }
        },
        async submitComment() {
            try {
                    const that = this
                    const res = await this.$http.put(
                        '/escBackend/comment/'+this.comment_object.id + '/',
                        {
                            Stage: 1,
                            Writer: 1,
                            Context: that.comment_object.Context,
                            Pass_Fail: that.pass_fail,
                            Submited: true
                        }
                    );
                    // location.reload();

                    return res.data.results
            }catch(e) {
                window.console.log(e);
            }
        },
    }

}
</script>
