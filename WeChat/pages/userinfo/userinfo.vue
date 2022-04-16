<template>
	<view class="container">
		<u-navbar back-text="返回" ></u-navbar>
		<view class="box_title">
			<text>修改个人信息</text>
		</view>
		<view class="goReg">
			<!-- <navigator url="../login/login"><text>已有账号?去登录</text></navigator> -->
		</view>
		<view class="box_form">
			<u-form :model="form" ref="uForm">
				<u-form-item label="用户账号" disabled label-position="top" prop="userID"><u-input v-model="form.userID" placeholder="请输入用户账号" /></u-form-item>
				<u-form-item label="用户密码" disabled label-position="top" prop="passWord"><u-input v-model="form.passWord" placeholder="请输入用户密码" /></u-form-item>
				<!-- <u-form-item label="确认密码" label-position="top" prop="confirmPassWord"><u-input v-model="form.confirmPassWord" placeholder="请输入用户密码" /></u-form-item> -->
				
				<u-form-item label="用户昵称" label-position="top" prop="nickName"><u-input v-model="form.nickName" placeholder="请输入用户昵称" /></u-form-item>
				<u-form-item label="用户姓名" label-position="top" prop="userName"><u-input v-model="form.userName" placeholder="请输入用户姓名" /></u-form-item>
				
				
			</u-form>	
			
		</view>
		<view class="faceUpload">
			<u-form-item label="人脸信息上传" label-position="top" prop="faceInfo">
				
				<u-upload :file-list="fileList" ></u-upload>
			</u-form-item>
			
		</view>
		
		
		<view class="sub_reg">
			<u-button type="primary" @click="Onsub_reg">修改</u-button>
		</view>
		
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				fileList: [],
				form:{
					userID:'123456',
					passWord:'******',
					confirmPassWord:'',
					nickName:'',
					userName:'麒麟',
					faceInfo:{}
				},
				rules: {
					userID: [
						{ 
							required: true, 
							message: '请输入用户账号', 
							// 可以单个或者同时写两个触发验证方式 
							trigger: ['change','blur'],
						}
					],
					passWord: [
						{
							required: true, 
							message: '请输入用户密码', 
							// 可以单个或者同时写两个触发验证方式 
							trigger: ['change','blur'],
						},
						{
							max: 32, 
							message: '用户密码最长为32位', 
							trigger: 'change'
						}
					]
				},
				xieyi:{
					checked:false,
					name: 'xieyi',
				}
			}
		},
		onReady() {
			this.$refs.uForm.setRules(this.rules);
		},
		methods: {
			OnXieyi(){
				console.log('点击了用户协议')
			},
			Onsub_reg(e){
				console.log('用户点击了注册')
				
				this.$refs.uForm.validate(valid => {
					if (valid) {
						console.log('验证通过');
						
					} else {
						console.log('验证失败');
					}
				});
				
			}
		}
	}
</script>

<style scoped lang="scss">
	.container {
		padding: 40rpx;
		.box_title {
			
			text {
				font-size: 22px;
				font-weight: 700;
			}
		}
		.box_form {
			// margin-top: 20rpx;
			
			.box_input {
				margin-bottom: 45rpx;
				.input_val {
					margin-top: 10rpx;
					border-bottom: .5px solid #eee;
					padding: 20rpx 0rpx;
					.pal {
						font-size: 15px;
						color: #aaaaaa;
					}
				}
			}
			
		}
		.xieyi {
			margin-top: 45rpx;
		}
		
		.sub_reg {
			margin-top: 45rpx;
		}
		.goReg {
			margin-top: 10rpx;
			color: #2979ff;
			font-size: 14px;
		}
	}
</style>
