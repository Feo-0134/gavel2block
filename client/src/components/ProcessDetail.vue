<template>
    <v-container>
        <!-- {{process_object}} -->
        <!-- <Process :process_object= "process_object" /> -->
        <v-timeline dense>
            <v-timeline-item
            v-for="n in items"
            :key="n"
            v-show="n.stage <= cntStage"
            color="red lighten-2"
            large
            >
            <template v-slot:opposite>
                <span>Tus eu perfecto</span>
            </template>
            <v-card class="elevation-2">
                <v-row>
                <v-card-title class="headline ml-5">
                    {{n.title}}
                </v-card-title>
                <v-spacer></v-spacer>
                <v-btn v-show="n.state==-1" large elevation="17" class="mt-3 mr-9" color="blue" outlined align="center">Pending</v-btn>
                <v-btn v-show="n.state==0" large elevation="17" class="mt-3 mr-9" color="red" outlined align="center">Fail</v-btn>
                <v-btn v-show="n.state==1" large elevation="17" class="mt-3 mr-9" color="green" outlined align="center">Pass</v-btn>
                </v-row>
                <v-row>
                    <v-card
                        class="mx-10"
                        color="#303030"
                        tile >
                        <v-app-bar
                        dark
                        color="#E57373"
                        >
                        <v-toolbar-title>Stage Context</v-toolbar-title>

                        <v-spacer></v-spacer>

                        <v-btn icon>
                            <v-icon>mdi-magnify</v-icon>
                        </v-btn>
                        </v-app-bar>

                        <v-container>
                        <v-row dense>
                            <v-col cols="12">
                                <v-card
                                    dark
                                    >
                                    <v-card-title class="headline">Upload Material</v-card-title>

                                    <v-card-subtitle>Please list your material here for the reviewers and admins to check-out.</v-card-subtitle>
                                    <v-file-input class="mx-5" multiple label="File input"></v-file-input>
                                    <v-card-actions>
                                    <v-btn text>Submit</v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-col>
                        </v-row>
                        </v-container>
                    </v-card>
                <v-col>
                <v-row>
                    <v-col v-for="m in comment_list" v-show="m.Stage === n.stage && n.stage != 1 && (n.stage < cntStage || m.Writer == $store.state.id)"
                        :key="m" 
                        >
                    <Comment :comment_object="m" />
                    </v-col>
                </v-row>
                </v-col>
                </v-row>
                <v-row
                        align="center"
                        justify="start"
                        >
                    <v-btn class="ml-10 mt-5" v-show="$store.state.role === 'reviewer' && n.stage != 1 && n.stage === cntStage && !madeComment[n.stage]" color="#E57373" @click="newComment(n.stage)">
                        New comment
                    </v-btn>
                    <!-- <v-spacer></v-spacer> -->
                    <!-- <v-btn class="mr-3" v-show="$store.state.role === 'admin'" color="primary" @click="enterNewStage('pass')">
                        Stage pass
                    </v-btn>
                    <v-btn class="mr-10" v-show="$store.state.role === 'admin'" color="primary" @click="enterNewStage('fail')">
                        Stage fail
                    </v-btn> -->
                </v-row>
                <v-card-text>
                    <!-- {{n.state}}{{$store.state.role === 'reviewer'}} {{n.stage != 1}} -->
                </v-card-text>
            </v-card>
            </v-timeline-item>
        </v-timeline>
    </v-container>
</template>
<script>
import Comment from '@/components/Comment'
export default {
    props: { },
    components: { Comment },
    data: () => ({
        cntStage: 0,
        items: [ ],
        currentStage: 0,
        madeComment: [0],
        data_updated: false
    }),
    asyncComputed: {
        stage_list: {
            async get() {
                try {
                    const res = await this.$http.get(`/escBackend/stage_kind/`)
                    
                    return res.data.results
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        process_object: {
            async get() {
                try {
                    const res = await this.$http.get(`/escBackend/process/${this.process_id}`)
                    this.currentStage = res.data.ProcessCurrentStage
                    let Stage1TryTimes = res.data.Stage1TryTimes
                    let Stage2TryTimes = res.data.Stage2TryTimes
                    let Stage3TryTimes = res.data.Stage3TryTimes
                    let Stage4TryTimes = res.data.Stage4TryTimes
                    this.items = []
                    while(Stage1TryTimes && Stage1TryTimes>0) {
                        this.cntStage++
                        this.items.push(
                            {
                                stage: this.cntStage,
                                title: this.stage_list[0].FullName,
                                state: 0
                            }
                        )
                        Stage1TryTimes--
                    }
                    let l = this.items.length
                    this.items[l - 1].state = 1
                    while(Stage2TryTimes && Stage2TryTimes>0) {
                        this.cntStage++
                        this.items.push(
                            {
                                stage: this.cntStage,
                                title: this.stage_list[1].FullName,
                                state: 0
                            }
                        )
                        Stage2TryTimes--
                    }
                    l = this.items.length
                    this.items[l - 1].state = 1
                    while(Stage3TryTimes && Stage3TryTimes>0) {
                        this.cntStage++
                        this.items.push(
                            {
                                stage: this.cntStage,
                                title: this.stage_list[2].FullName,
                                state: 0
                            }
                        )
                        Stage3TryTimes--
                    }
                    l = this.items.length
                    this.items[l - 1].state = 1
                    while(Stage4TryTimes && Stage4TryTimes>0) {
                        this.cntStage++
                        this.items.push(
                            {
                                stage: this.cntStage,
                                title: this.stage_list[3].FullName,
                                state: 0
                            }
                        )
                        Stage4TryTimes--
                    }
                    l = this.items.length
                    this.items[l - 1].state = 1
                    l = this.items.length
                    if(res.data.Finished != true) this.items[l - 1].state = -1
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            },
            watch:['data_updated']
        },
        comment_list: {
            async get(){
                try {
                    const that = this
                    let flag = false
                    let commentArray = []
                    this.madeComment = []
                    // window.console.log(this.process_object.ProcessComments)
                    for (let n=0;n<this.process_object.ProcessComments.length;n++) {
                        const res = await this.$http.get(`/escBackend/comment/${that.process_object.ProcessComments[n]}`)
                        if (res.data.Writer == that.$store.state.id) {
                            flag = true
                        }
                        commentArray.push(res.data)
                        this.madeComment.push(flag)
                        flag = false
                    }
                    // window.console.log(commentArray)
                    
                    return commentArray
                }catch(e) {
                    window.console.log(e)
                }
            },
            watch:['process_object'],
        },
    },
    computed: {
        process_id: function() {
            let current_id = this.$router.currentRoute.path.split("/")[2]
            // window.console.log(current_id)
            return current_id
        }
    },
    beforeMount() {
        
    },
    methods: {
        async newComment(stage) {
            try {
                    const that = this
                    const res = await this.$http.post(
                        '/escBackend/comment/',
                        {
                            Stage: stage,
                            Writer: that.$store.state.id,
                            Context: 'template context',
                            Pass_Fail: -1,
                            Submited: false
                        }
                    );
                    window.console.log(res.data)
                    const res1 = await this.$http.post(
                        '/escBackend/process_comment/',
                        {
                            Process: that.process_id,
                            Comment: res.data.id
                        }
                    );
                    // location.reload();
                    this.data_updated = true
                    return res1.data
            }catch(e) {
                window.console.log(e);
            }
        },
        async enterNewStage(status) {
            try {   
                    this.cntStage++
                    
                    if(status == 'pass') {
                        this.process_object.ProcessCurrentStage += 1
                        if (this.process_object.Stage2TryTimes === -1) this.process_object.Stage2TryTimes = 1
                        else if (this.process_object.Stage3TryTimes === -1) this.process_object.Stage3TryTimes = 1
                        else if (this.process_object.Stage4TryTimes === -1) this.process_object.Stage4TryTimes = 1
                    }else if(status == 'fail') {
                        if (this.process_object.Stage2TryTimes === -1) this.process_object.Stage1TryTimes += 1
                        else if (this.process_object.Stage3TryTimes === -1) this.process_object.Stage2TryTimes += 1
                        else if (this.process_object.Stage4TryTimes === -1) this.process_object.Stage3TryTimes += 1
                        else this.process_object.Stage4TryTimes += 1
                    }
                    this.items.push(
                        {
                            stage: this.cntStage,
                            title: this.stage_list[this.process_object.ProcessCurrentStage-1].FullName
                        }
                    )   
                    const that = this
                    const res = await this.$http.put(
                        '/escBackend/process/' + that.process_object.id + '/',
                        {
                            Kind: that.process_object.Kind,
                            ProcessOwner: that.process_object.ProcessOwner,
                            ProcessReviewer: that.process_object.ProcessReviewer,
                            ProcessComments: that.process_object.ProcessComments,
                            ProcessCurrentStage: that.process_object.ProcessCurrentStage,
                            Stage1TryTimes: that.process_object.Stage1TryTimes,
                            Stage2TryTimes: that.process_object.Stage2TryTimes,
                            Stage3TryTimes: that.process_object.Stage3TryTimes,
                            Stage4TryTimes: that.process_object.Stage4TryTimes
                        }
                    );
                    window.console.log(res.data.results)
                    // location.reload();
                    return res.data.results
            }catch(e) {
                window.console.log(e);
            }
        },
    }

}
</script>